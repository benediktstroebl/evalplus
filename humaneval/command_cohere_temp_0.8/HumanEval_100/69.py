```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Loop to create subsequent levels
    for i in range(1, n):
        if i % 2 == 1:
            pile.append(i + 2)
        else:
            pile.append(i + 1)
    
    return pile
```

This Python script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function returns a list where each element represents the number of stones in each level of the pile. The logic for determining the number of stones in the next level is encapsulated within the loop, where the parity of the loop index `i` determines whether the next level has an odd or even number of stones.