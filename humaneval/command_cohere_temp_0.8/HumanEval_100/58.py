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
The function uses a loop to create a list-based "pile" of stones, adding the next level's stone count based on whether the previous level's count was even or odd, following the problem's definition. This process continues until the pile has `n + 1` levels, ensuring it's of the correct size to start.