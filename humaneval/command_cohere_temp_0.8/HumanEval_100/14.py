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
The function uses a loop to generate the pile level by level, alternating between adding 1 and 2 to the previous level count based on whether it's odd or even. The result is a list representing the count of stones for each level.