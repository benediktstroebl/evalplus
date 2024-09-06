```python
def make_a_pile(n):
    # Initialize a list to store the pile sizes
    pile = [n]
    
    # Loop to create subsequent levels
    for i in range(1, n):
        if i % 2 == 1:
            pile.append(i + 2)
        else:
            pile.append(i + 1)
    
    return pile
```

This approach uses a simple loop to create the pile levels, determining the next level's size based on whether the current level's size is even or odd and then appending the size to the pile list. It creates the pile incrementally for each level.