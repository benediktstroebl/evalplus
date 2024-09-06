```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        elif len(pile) % 2 == 1 or pile[-1] % 2 == 1:
            pile.append(pile[-1] + 1)
        else:
            raise Exception("Can't reach this statement")
    return pile
```

The code uses a simple `while` loop that appends to a starter list (`pile`) with the next stone value based on the criteria described in the problem. The loop runs until the pile's length is `n + 1`, ensuring there are `n + 1` levels in the pile. The result is returned as a list, where each element represents the number of stones in the corresponding level.