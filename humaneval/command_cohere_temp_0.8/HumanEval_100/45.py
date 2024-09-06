```python
def make_a_pile(n):
    # Generate the sequence of stone counts for each level in the pile.
    pile = [n]
    while len(pile) < n:
        # If the previous level has an even number of stones,
        # the next level has this many stones.
        if len(pile) % 2 == 0:
            pile.append(pile[-1] + 2)
        # If the previous level has an odd number of stones,
        # the next level has this odd number of stones.
        else:
            pile.append(pile[-1] + 1)
    return pile
```