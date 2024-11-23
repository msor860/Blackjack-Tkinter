import random
import tkinter
def load_images(card_images):
  suits = ['hearts', 'clubs', "diamonds", 'spades']
  face_cards = ['jack', 'queen', 'king']
  for suit in suits:
    
    for card in range(1,11):
      name = 'cards/{}-{}.{}'.format(str(card), suit, 'png')
      #print(name)
      image = tkinter.PhotoImage(file=name)
      card_images.append((card,image))

    for card in face_cards:
      name = 'cards/{}-{}.{}'.format(str(card), suit, 'png')
      #print(name)
      image = tkinter.PhotoImage(file=name)
      card_images.append((10,image))
    
def deal_card(frame):
  #pop the next card off the top of the deck
  next_card = deck.pop(0)
  # and add it to back of the pack
  deck.append(next_card)
  # add the image to a Label and display the Label
  tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
  # now return the card's face Value
  return next_card

def score_hand(hand):
  #Calculate the total score of all cards in the list.
  #Only one ace can have the value 11, and this will be reduced to 1 if the hand would bust.
  score = 0
  ace = False
  for next_card in hand:
    card_value = next_card[0]
    if card_value == 1 and not ace:
      ace = True
      card_value = 11
    score += card_value
    #if we would bust, check if there is an ace and substract 10
    if score > 21 and ace:
      score -= 10
      ace = False
  return score

def deal_dealer():
  dealer_score = score_hand(dealer_hand)
  while 0 < dealer_score < 17:
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)

  player_score = score_hand(player_hand)
  if player_score > 21:
    result_text.set("Dealer wins!")
  elif dealer_score > 21 or dealer_score < player_score:
    result_text.set("Player wins!")
  elif dealer_score > player_score:
      result_text.set("Dealer wins!")
  else:
    result_text.set("Draw!")
  if len(result_text.get()) > 0:
    player_button.configure(state=tkinter.DISABLED)
    dealer_button.configure(state=tkinter.DISABLED)

def deal_player():
  player_hand.append(deal_card(player_card_frame))
  player_score = score_hand(player_hand)
  player_score_label.set(player_score)
  if player_score > 21:
    result_text.set("Dealer Wins!")
    if len(result_text.get()) > 0:
      player_button.configure(state=tkinter.DISABLED)
      dealer_button.configure(state=tkinter.DISABLED)

def new_game():
  global dealer_card_frame
  global player_card_frame
  global dealer_hand
  global player_hand
  global dealer_button
  global player_button
  #embendded frame to hold the card images
  dealer_card_frame.destroy()
  dealer_card_frame = tkinter.Frame(card_frame, background = 'green')
  dealer_card_frame.grid(row=0, column=1, sticky = 'ew', rowspan=2)
  #embendded frame to hold the card images
  player_card_frame = tkinter.Frame(card_frame, background = 'green')
  player_card_frame.grid(row=2, column=1, sticky = 'ew', rowspan=2)
  result_text.set("")
  player_button.configure(state=tkinter.NORMAL)
  dealer_button.configure(state=tkinter.NORMAL)
  #Create the list to sotre("sort" with french accent) the dealer's and player's hands
  dealer_hand = []
  player_hand = []

  deal_player()
  dealer_hand.append(deal_card(dealer_card_frame))
  dealer_score_label.set(score_hand(dealer_hand))
  deal_player()

def shuffle():
  random.shuffle(deck)

root = tkinter.Tk()
#set up the screen and frames for the dealer and player
root.title("Black Jack")
root.geometry("640x480")
root.configure(background = 'green')

result_text = tkinter.StringVar()
result = tkinter.Label(root, textvariable=result_text)
result.grid(row=1, column=2, pady=20, columnspan=3)

card_frame = tkinter.Frame(root, relief="sunken", borderwidth=1, background='green')
card_frame.grid(row=2, column=2, padx = 20, sticky='w', columnspan = 3, rowspan = 2)

dealer_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Dealer", background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)
#embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background = 'green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)


player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)
#embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background = 'green')
player_card_frame.grid(row=2, column=1,sticky='ew', rowspan=2)

button_frame = tkinter.Frame(root)
button_frame.grid(row=4, column=2, padx=20, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=2)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=3)

new_game_button = tkinter.Button(button_frame, text="New Game", command = new_game)
new_game_button.grid(row=0, column=4)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=5)

#load_cards
cards = []
load_images(cards)
#print(cards)
#Create a new deck of cards and shuffle them
deck = list(cards) + list(cards) + list(cards)
shuffle()
#Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

new_game()

root.mainloop()