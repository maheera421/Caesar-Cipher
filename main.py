import art
import sheet


def caesar():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift % 26
      
  end_text = ""
    
  if direction == "decode":
    shift *= -1
      
  for char in text:
   #if the user enters a number/symbol/space?
    if char not in sheet.alphabet:
        end_text += char
      
    position = sheet.alphabet.index(char)
    new_position = position + shift
    end_text += sheet.alphabet[new_position]
    
  print(f"Here's the {direction}d result: {end_text}")

def restart():
  rep = True
  while rep:
    answer = input("Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
      
    if answer == "yes":
        caesar()
    elif answer == "no":
        rep = False  #to stop the loop


print(art.logo)

caesar()
restart()