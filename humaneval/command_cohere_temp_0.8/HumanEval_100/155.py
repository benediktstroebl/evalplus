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
The function uses a simple iterative approach to create the pile, ensuring the stones follow the prescribed pattern. Each element in the `pile` represents the number of stones in a respective level. The loop continues until the pile has the required number of levels (`n + 1`). At the end, the function returns the list `pile`, where each element represents the number of stones in a corresponding level.