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
The function uses a loop to generate the next levels of the pile until reaching the required number of levels (`n + 1`). It follows the given rules for incrementing the stone count at each level, using recursion to calculate the next even or odd number respectively. 

The `make_a_pile` function returns the list of stone counts for each level, ensuring that the element at index `i` represents the number of stones in the level (`i + 1`).