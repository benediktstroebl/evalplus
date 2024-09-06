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
This Python script defines a function called `make_a_pile` that takes a single argument, `n`, which represents the number of stones in the first level of the pile. The function returns a list of stone counts for each level of the pile. It starts with `n` stones in the first level, and for each subsequent level, it adds 1 to the previous count if the previous count was odd, or adds 2 to the previous count if the previous count was even.