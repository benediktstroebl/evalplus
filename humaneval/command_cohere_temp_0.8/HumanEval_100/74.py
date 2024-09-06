```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This code defines a function make_a_pile() that takes a positive integer n as input and creates a list of the number of stones in each level of a pile of 'n' levels of stones according to the problem description. It starts with 'n' stones on the first level, and for each subsequent level, it adds 1 to the previous level's count if 'n' is odd, and 2 if 'n' is even, until it reaches the next peak level. The result is a list of stone counts for each level, including the peak level, which is returned.