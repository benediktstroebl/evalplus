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
This Python script defines a function named `make_a_pile` that addresses the problem statement. It takes a single argument `n`, representing the number of stones in the first level of the pile. The function creates a list called `pile`, where each element represents the number of stones in each level.

To achieve this, it initializes `pile` with the first level of `n` stones and then enters a loop that continues until the length of the `pile` reaches `n+1` (the number of levels specified in the problem). Within each iteration, it either increments or decrements the previous count (based on whether it's even or odd) and adds the updated count to the next level.

Finally, it returns the `pile` list, which now contains the number of stones required for each level of the pile.