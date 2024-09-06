```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]

    # Loop through and calculate the number of stones for each level based on the given rules
    for l in range(1, n + 1):
        if l % 2 == 0 and pile[l // 2] % 2 == 1:
            pile.append(pile[l // 2] + 1)
        elif l % 2 != 0 and pile[l // 2] % 2 == 0:
            pile.append(pile[l // 2] + 2)

    return pile
```

This Python script defines a function, `make_a_pile(n)`, that takes a positive integer command and creates a list of stones for each level of a pile. It starts with the base case of `n` stones in the first level, then loops through each level, calculating the number of stones for the next level based on the parity of the current level `l` and the previous level's parity. This is done to ensure the pile grows in a consecutive and consistent manner.