```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This code defines a function make_a_pile() that takes a positive integer n as input and creates a pile of stones as described in the problem statement. It starts with a base level of n stones and iteratively calculates the number of stones for the next level by adding 1 if the current level is even, or 2 if the current level is odd. It does this while looping until the number of levels equals n + 1. The resulting list of stone counts is returned as the output pile.