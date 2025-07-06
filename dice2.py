import random

playagain=True
while playagain:
    playagain = input ('Throw dice? y or n: ')
    #computer=random.choice('123456')
    computer=random.randint(1,6)
    print (computer)
    
    if playagain.lower() == "y":
        continue
    else:
        print("\nThanks you for playing!\n")
        playagain = False
        # break


# i = 1
# while i < 1000:
#     input ('')
#     computer=random.choice('123456')
#     print (computer)
#     i += 1
