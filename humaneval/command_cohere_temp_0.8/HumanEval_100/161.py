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
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones needed for each level in the pile. The function returns a list where each element represents the number of stones for the corresponding level. It starts with `n` stones in the first level, and for each subsequent level, it adds 1 if the previous level had an odd number of stones, or 2 if the previous level had an even number of stones. This logic is repeated until the pile reaches the desired number of levels.