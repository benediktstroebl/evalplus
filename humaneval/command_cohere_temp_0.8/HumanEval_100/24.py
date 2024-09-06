```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```

This script defines a function `make_a_pile` that takes a positive integer `n` as input and returns a list representation of the pile, satisfying the given conditions. It uses a `while` loop to build the pile level by level, alternating between even and odd numbers, until it reaches the desired number of levels (`n + 1`). The `if` condition within the loop checks whether the current number is even and the previous number is even, in which case it increments the even number by 2 for the next level, or else it increments it by 1. Finally, it returns the list of stone counts for each level.