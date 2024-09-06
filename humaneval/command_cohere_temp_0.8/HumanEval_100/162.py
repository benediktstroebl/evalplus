```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This code defines a function make_a_pile() that takes a positive integer n as input and creates a pile of stones as described in the problem statement. It starts with a base level of n stones and then iteratively calculates the number of stones for the next level by adding 1 if the current level is odd, or 2 if the current level is even. The process continues until the pile reaches the desired number of levels (n + 1). The final result is a list containing the count of stones for each level, where the element at index i represents the number of stones in the (i + 1)th level.