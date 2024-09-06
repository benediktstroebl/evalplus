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
This Python script defines a function named `make_a_pile` that solves the problem through a recursive process. It starts with a list of just the base number of stones, then for each subsequent level adds either 1 or 2 stones, ensuring that each level has one more stone than the previous one.