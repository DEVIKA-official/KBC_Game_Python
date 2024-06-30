questions = [
    ["Nickname of Devika Is:", "Chintu", "Parul", "Gullu", "Devu", 1],
    ["Favourite Movie of Devika Is:", "romantic", "horror", "comedy", "all",4], 
    ["D.O.B of Devika Is:", "17-oct", "21 nov", "29-feb", "13-march", 1],
    ["Favourite food of Devika Is:", "sweets", "tangy", "bitter", "mix", 2],
    ["Gift for Devika Is:", "expensive", "decorations", "soft-toys","luxury", 3]
]

levels = [1000, 2500, 3000, 4500, 8000]
money = 0

for i in range(len(questions)):
  question = questions[i]
  print(f"\nQuestion for Rs.{levels[i]}")
  print(f"a. {question[1]}        b. {question[2]}")
  print(f"c. {question[3]}        d. {question[4]}")

  reply = int(input("Enter your answer (1-4) or 0 to 'quit' : "))
  if (reply == 0):
   money = levels[i - 1]
   break

  if reply == question[5]:
    money = levels[i]
    print(f"Correct Answer 😋 !!\nYou have won Rs. {money} 🤑")
  else:
    print("Wrong Answer 😥")
    break

print(f"You have won a total of Rs. {money}")
