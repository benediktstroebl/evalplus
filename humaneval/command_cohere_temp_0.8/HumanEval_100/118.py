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
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones needed for each level in the pile. The function returns a list where each element represents the number of stones for the corresponding level. It initially creates a foundation with 'n' stones and then iteratively constructs the next levels. If the current level is even, it adds 2 stones, and if it's odd, it adds 1 stone. The condition `len(pile) < n+1` ensures that the loop terminates after 'n' levels, and the pile size is updated accordingly in each iteration.