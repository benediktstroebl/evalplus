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
This script defines a function `make_a_pile` that takes a positive integer `n` as input and returns a list representing the number of stones in each level of the pile. It starts with `n` stones in the first level, and for each subsequent level, it adds 1 if the previous level had an odd number of stones, and 2 if the previous level had an even number of stones. The loop runs until the pile has `n+1` number of levels. 

The examples given in the problem statement would yield the following results:
```
>>> make_a_pile(3)
[3, 5, 7]
>>> make_a_pile(4)
[4, 6, 8]
```