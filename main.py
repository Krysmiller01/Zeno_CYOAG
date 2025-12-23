def scene1():
    print("You are Zeno, the great philosopher of 300 BC. Zeno is a man who walks the earth questioning everything in front of him.")
    print("The city square has a building for sale, you say. The building is old, needing a fresh coat of paint and spiders in every corner. Your gut says this is it, but should you trust that?")
    print("\nChoices:")
    print("1: It will do")
    print("2: Let's at least talk it over")

    choice1 = input("What will you do? (Enter 1 or 2): ")

    if choice1 == "1":
        print("\nYou buy the building and gather your friend Dorth of Citium. He is a man of few words and many talents. He listens well and you both build the old square building into a livable quarters for yourself.")
        scene2()
    elif choice1 == "2":
        print("\nThe owner scoffs and ignores your asking of features. 'You want it or not? We have 3 people coming over the next 2 hours and whoever says yes first gets it.' You don’t hesitate further. You buy the building, thinking to trust your gut next time. You gather your friend Dorth of Citium. He is a man of few words and many talents. He listens well and you both build the old square building into a livable quarters for yourself.")
        scene2()
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
        scene1()

def scene2():
    print("\nYou stand on your new porch, reading over your papers on the house sale. The city is having a market in the front of the building. There are various vegetables for sale right in front of your porch. The stand is facing the same direction as you, so you mostly see a man’s backside. The man is trying to sell carrots to an older woman. You briefly see his nose, huge. There is no way he can see his feet with that honker. A brief second later a child walking in between your porch and the stand quickly turns and while keeping his hands close to the waist of the vegetable man, swiftly snatches an apple off the stand. Your eyes perk up, the kid’s eyes meet yours.")

    print("\nChoices:")
    print("1: Yell after the child")
    print("2: Ignore the scene")
    print("3: Chase the child")

    choice2 = input("What will you do? (Enter 1, 2, or 3): ")

    if choice2 == "1":
        print("\nYou yell out, but it was too late. The child went around the building so fast, it was useless. The market in front of you is too loud for anyone but even just the few walkers in front of you to notice.")
        end_game()
    elif choice2 == "2":
        print("\nYou smile at the child. He smiles back, then runs around the building. It seems he was aware of so much, the blind spot, the apple's location. It was not his first time doing this exact crime.")
        end_game()
    elif choice2 == "3":
        print("\nYou get up, the child runs around your building. You follow up until you bump into a courtesan and she pushes you back calling you a woman handler. You profusely apologize and turn back to your new home with a bit more shame. You wonder why you made that choice anyway. What was the goal of catching the apple thief?")
        end_game()
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")
        scene2()

def end_game():
    print("\nThe story ends here. Thanks for playing!")
    exit()

# Start the adventure
scene1()
