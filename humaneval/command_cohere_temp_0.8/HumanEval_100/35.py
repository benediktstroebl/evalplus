```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 0:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
The function uses a loop to generate the stones pile level by level, alternating between even and odd numbers, and appends each level's stone count to the pile list. The process continues until the pile has `n + 1` levels, ensuring the final result matches the specified requirement.