def count_wins(dice1, dice2):                       # Create a function to find how many times each dice wins.
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for x in dice1:
        for y in dice2:
            if x > y:
                dice1_wins += 1
            elif x < y:
                dice2_wins += 1
    return dice1_wins, dice2_wins                  # Return the value of wins for each dice.

# Use the following to debug the fuction above.
# Input: dice1 = [1, 2, 3, 4, 5, 6], dice2 = [1, 2, 3, 4, 5, 6]
# Output: (15, 15)


def find_the_best_dice(dices):                     # Create a function to find which dice wins the most.
    assert all(len(dice) == 6 for dice in dices)
    wins = [0]*len(dices)                          # Create an empty array with spaces equivalent to the number of dices.
    for x in range(len(dices)):                    # Compare 2 dices and store the number of times each dice wins into the array wins[].
        for y in range(x + 1, len(dices)):
            a, b = count_wins(dices[x], dices[y])
            if a > b:
                wins[x] += 1
            else:
                wins[y] += 1
    check = True
    elem = wins[0]
    for x in wins:                                 # Check if there is a duplicate number of wins for each dice.
        if elem != wins[x]:
            check = False

    if check is True:
        return -1                                  # Returns -1 if there is no best dice
    elif check is False:
        max_int = max(wins)
        max_index = wins.index(max_int)
        if max_index != 0:
            for x in range(0, wins[max_index]):
                if wins[max_index] == wins[x]:
                    check = True
        for x in range(max_index + 1, len(wins)):
            if wins[max_index] == wins[x]:
                check = True
        if check is True:
            return -1                              # Returns -1 if there is no best dice
        else:
            return max_index                       # Return the dice which wins the most
        
# Use the following to debug the fuction above.
# Input: [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
# Output: -1


def compute_strategy(dices):                       # Create a function that finds the best dice which is most likely to win against another dice.
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True                # Determine whether the user is going first or second.

    if find_the_best_dice(dices) != -1:            # Make sure that there is a best dice among the dices listed.
        strategy["choose_first"] = True
        strategy["first_dice"] = find_the_best_dice(dices)
    else:
        strategy["choose_first"] = False
        for x in range(len(dices)):
            for y in range(len(dices)):
                dice1_win, dice2_win = count_wins(dices[x], dices[y])
                if dice1_win < dice2_win:
                    break
            strategy[x] = y

    return strategy                                # Return the best dice that the user can choose to win.

# Use the following to debug the fuction above.
# Input: [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
# Output: {'choose_first': True, 'first_dice': 1}

# Use the code below to input the values of the dices before running the code.
# Dices = [[?, ?, ?, ?, ?, ?], [?, ?, ?, ?, ?, ?], ...]
# print(compute_strategy(dices))
