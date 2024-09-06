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
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function generates a list (`pile`) where each element represents the number of stones in a respective level of the pile. It starts with `n` stones in the first level and iteratively calculates the number of stones for the next level. If the current level has an odd number of stones (`len(pile) % 2 == 1`), the next level will have `n + 2` stones. If the current level has an even number of stones, the next level will have `n + 1` stones. This process continues until the total number of levels reaches `n + 1`, and the `pile` list is returned.