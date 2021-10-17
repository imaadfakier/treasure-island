print('''
       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
''')
print("Welcome to Hitman Island.")
print("Your mission is to escape.")

left_or_right_handed = input("Here's a trick question, \"left\" or \"right\"? \n").casefold()

#print(left_or_right_handed)

if (left_or_right_handed == "left"):
  to_jump_or_not_to_jump = input("Lucky break. Will you \"jump\" or will you \"give in to temptation\"? \n").lower()

  if (to_jump_or_not_to_jump == "jump"):
    red_yellow_or_blue = input("All you have are three doors - \"red\", \"yellow\" and \"blue\" - which of the three shall it be? \n").casefold()

    if (red_yellow_or_blue == "red"):
      print("Hahaha, your soul is mine. Game over.")
    elif (red_yellow_or_blue == "yellow"):
      print('Damn it! Damn it! I thought for sure I got you! You win.')
    else:
      print("I was right. Your streak of \"god\" fortune has come to a halt. Game ... over.")

  elif (to_jump_or_not_to_jump == "give in"):
    print("The urge. That's your weakness ... typical. Game over.")
else:
  print("Well, well, well ... not keen on escaping? Fine by me. Game over.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload