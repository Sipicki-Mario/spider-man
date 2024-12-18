import random


def spider_man_game():
    print("Welcome to the Spider-Man text-based game!")

    player_health = 100
    goblin_health = 50
    spider_sense = False

    while player_health > 0 and goblin_health > 0:
        print("\nYour health: ", player_health)
        print("Goblin's health: ", goblin_health)

        action = input("\nChoose an action - 1. Attack, 2. Defend, 3. Spider Sense: ")

        if action == '1':  # Attack
            player_attack = random.randint(10, 20)
            goblin_attack = random.randint(5, 15)

            goblin_health -= player_attack
            player_health -= goblin_attack

            print("You attacked the goblin and dealt", player_attack, "damage.")
            print("The goblin attacked you and dealt", goblin_attack, "damage.")

        elif action == '2':  # Defend
            player_block = random.randint(5, 10)
            goblin_attack = random.randint(5, 15)

            player_health -= max(0, goblin_attack - player_block)

            print("You blocked the goblin's attack and took", max(0, goblin_attack - player_block), "damage.")

        elif action == '3':  # Spider Sense
            spider_sense = True
            print("You activated Spider Sense! The goblin's next attack will miss.")

        else:
            print("Invalid action. Please choose a valid action.")
            continue

        if goblin_health <= 0:
            print("Congratulations! You defeated the goblin.")
        elif player_health <= 0:
            print("Game over. The goblin defeated you.")

    print("\nThanks for playing!")


spider_man_game()