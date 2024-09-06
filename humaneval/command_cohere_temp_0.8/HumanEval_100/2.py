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
This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. It constructs a list `pile` with the first element being `n` and then iteratively calculates the number of stones for the next level based on whether the previous level's count was even or odd. It continues this process until `pile` contains `n+1` elements, representing the number of stones in each level of the pile. The final result is the list `pile`.