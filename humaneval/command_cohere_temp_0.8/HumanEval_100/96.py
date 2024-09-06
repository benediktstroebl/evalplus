```python
def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]
    
    # Loop to create additional levels
    for i in range(1, n // 2 + 1):
        # If the current level is even, increment the previous even level
        if i % 2 == 0:
            pile.append(pile[-1] + 2)
        # If the current level is odd, increment the previous odd level
        else:
            pile.append(pile[-1] + 1)
    
    return pile
```

This Python script defines a function, `make_a_pile(n)`, which takes a single argument, `n`, representing the number of stones in the first level of the pile. The function returns a list where the first element represents the number of stones in the first level (`n`), and each subsequent element represents the number of stones in the next level. The logic within the function iteratively creates subsequent levels of the pile based on whether the current level is even or odd, incrementing the previous level by 1 or 2 respectively.