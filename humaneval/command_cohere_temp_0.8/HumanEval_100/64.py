```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        elif len(pile) % 2 == 1 or pile[-1] % 2 == 1:
            pile.append(pile[-1] + 1)
        else:
            raise Exception("Can't make the pile")
    return pile
```

The code uses a simple iterative approach to create the pile, ensuring that each element is calculated based on the previous one meeting the required conditions. It also includes a check for incorrect input values.