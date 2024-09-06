```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones needed at the base of the pile. The function constructs a list (`pile`) where each element represents the number of stones required for each level of the pile. It starts with `n` stones on the first level, and then iteratively calculates the number of stones for the next level based on whether `n` is odd or even. It ensures that the total number of stones aligns with the problem's requirement, and the result is returned as a list of stone counts for each pile level.