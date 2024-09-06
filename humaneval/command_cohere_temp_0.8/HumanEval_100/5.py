```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This code defines a function make_a_pile() that takes a positive integer n as input and returns a list representing the number of stones in each level of the pile. It starts with n stones on the first level, and for each subsequent level, it adds 1 to the previous level's count if n is even, and adds 2 to the previous level's count if n is odd, creating a growing pile effect.