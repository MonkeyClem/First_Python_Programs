import random

top_of_range = input("Please type a number : ")

if top_of_range.isdigit(): 
    top_of_range = int(top_of_range); 

    if top_of_range <= 0 : 
            input('Please, write a number larger than 0 next time !')
            quit()
else :
      print("Please type a number next time")
      quit()

random_number = random.randint(0, top_of_range)
print(random_number)