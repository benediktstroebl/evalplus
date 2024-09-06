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
The function uses a loop to generate the next levels of the pile until reaching the target number of levels (`n + 1`). If the length of the pile is even, it adds 2 to the previous level's size; if it's odd, it adds 1. The results are stored in a list, `pile`, ensuring that each element represents the number of stones for the subsequent level.