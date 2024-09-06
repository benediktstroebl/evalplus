```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if n % 2 == 1:
            n += 2
            pile.append(n)
        else:
            n += 1
            pile.append(n)
    return pile
```
This code defines a function make_a_pile() that takes a positive integer n as input and returns a list representing the number of stones in each level of the pile. It starts with n stones on the first level, and for each subsequent level, it increments n by 1 if it's odd or by 2 if it's even, and adds that value to the pile. This generates the required list of stone counts for each level, up to the (n+1)-th level.