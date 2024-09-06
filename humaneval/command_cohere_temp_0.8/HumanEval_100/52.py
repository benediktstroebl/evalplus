```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]

    # Loop through and calculate the number of stones for each level based on the given rules
    for l in range(1, n + 1):
        if l % 2 == 0 and pile[l % 2 - 1] % 2 == 1:
            pile.append(pile[l % 2 - 1] + 1)
        elif l % 2 != 0 and pile[l % 2 - 1] % 2 == 0:
            pile.append(pile[l % 2 - 1] + 2)

    return pile
```

This Python script defines a function, `make_a_pile(n)`, that takes a positive integer command and creates a list of stone counts for each level of a pile. The function initializes the list with the number of stones for the first level (n) before entering a loop that iterates through each subsequent level, determining the number of stones for that level based on the parity of the level number and the previous level's stone count. If the level is even and the previous level was odd, the count increases by 1; if the level is odd and the previous level was even, the count increases by 2. The final list returned represents the desired stone counts for each level.