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
This Python script defines a function called `make_a_pile` that takes a single argument, `n`, which represents the number of stones in the first level of the pile. The function returns a list of stone counts for each level of the pile. It starts with a single stone count of `n` and then iteratively calculates the number of stones for each subsequent level, always adding an odd number of stones if the pile is currently odd, or an even number of stones if the pile is currently even. This recursive process continues until the pile has reached a maximum of `n` levels, at which point the function returns the list of stone counts for each level.