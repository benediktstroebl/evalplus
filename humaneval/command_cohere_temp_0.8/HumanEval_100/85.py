```python
def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]
    
    # Loop to create subsequent levels
    for i in range(1, n):
        if i % 2 == 1:
            pile.append(i + 2)
        else:
            pile.append(i + 1)
    
    return pile
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level, and returns a list representing the number of stones in each subsequent level. It does so by iterating through odd and even numbers, adding 2 to the previous level's number of stones if the current level is odd, and adding 1 if the current level is even.