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
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function generates a list (`pile`) where each element represents the number of stones in a respective level of the pile. It starts with `n` stones in the first level, and then, iteratively, it calculates the number of stones for the next level based on whether the previous level's count was odd or even. The generated list is then returned, providing the number of stones for each subsequent level.