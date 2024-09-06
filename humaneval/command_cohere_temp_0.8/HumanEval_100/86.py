```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Loop to create each level of the pile
    for i in range(1, n+1):
        # If the current level is odd, the next level will contain the next odd number of stones
        if i % 2 == 1:
            pile.append(i + 1)
        # If the current level is even, the next level will contain the next even number of stones
        else:
            pile.append(i + 2)
    
    return pile
```

This Python script defines a function called `make_a_pile` that takes a single argument, `n`, representing the number of stones in the first level of the pile. The function creates a list called `pile` where each element represents the number of stones in a respective level of the pile. It iterates from the second level up to the `n+1`-th level, determining whether the current level is odd or even, and accordingly, calculates the number of stones for the next level. The resulting `pile` list is returned, indicating the number of stones in each level.