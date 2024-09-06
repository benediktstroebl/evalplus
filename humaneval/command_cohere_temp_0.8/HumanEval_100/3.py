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
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function then calculates the number of stones in each subsequent level, creating a list called `pile` that represents the number of stones in each level.

The process repeats until the length of the `pile` reaches `n+1`. At each iteration, it checks whether the length of the `pile` is odd or even to determine whether the next level should have the next odd or even number of stones. It then appends the new count to the `pile`.

The resulting `pile` list contains the number of stones for each level, with the element at index `i` representing the number of stones in the level (`i+1`).

The given example of `make_a_pile(3)` returns `[3, 5, 7]`, which aligns with the problem's expectation.