letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Zip the two variables into one zipped variable

letter_to_points = {letters:points for letters, points in zip(letters, points)}


# Add the blnank tile to the dictionary

letter_to_points["Blank"] = 0

# Use a function to find the score for the word "Lexicographical"

#def print_word(word):
  #for letters in word:
    #print(letters)

#print_word("Lexicographical")

#def score_word(word):
  #score = 0
  #for letters in word:
    #for letter in letters_to_point.values():

#score_word("Lexicographical")

#def score_word(word):
  #point_total = 0
  #for letters in word:
    #print(letters)
    #print(letter_to_points.get(letters, 0))
    #point_total += letter_to_points.get(letters, 0)
    #return point_total

#score_word("Lexicographical")

#def show_word(word):
  #point_total = 0
  #for letter in word:
    #print(letter)
    #print(letter_to_points.get(letter, 0))

#show_word("LEXICONICAL")

def score_word(word):
  point_total = 0
  for letter in word:
    #print(letter)
    #print(letter_to_points.get(letter, 0))
    point_total += letter_to_points.get(letter, 0)
    #print(point_total)
  return point_total

lexiconical_score = (score_word("LEXICONICAL"))

# Create a dictionary with the given players usernames and words

player_to_words = {
"playerone": ["BLUE", "TENNIS", "EXIT"],
"wordNerd": ["EARTH", "EYES", "MACHINE"],
"Lexi_Con": ["ERASER", "BELLY", "HUSKY"],
"Prof_Reader": ["ZAP", "COMA", "PERIOD"]
   }

player_to_points = {}

#for words in player_to_words:
  #for word in words:
    #player_score = 0
    #player_score += score_word(word)
  #return player_score

#for player, words in player_to_words.items():
  #player_points = 0
  #for word in words:
    #player_points += score_word(word)
  #player_to_points[player] = player_points
#print(player_to_points)

# Play a new word

#print(player_to_words)

def play_word(player, word):
  player_to_words[player].append(word)

play_word("playerone", "SCRABBLE")

#print(player_to_words)

# Update the total points

#print(player_to_points)

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print(player_to_points)

update_point_totals()
#print(player_to_points)


# Printing commands

print(letter_to_points)
print("")
print(lexiconical_score)

