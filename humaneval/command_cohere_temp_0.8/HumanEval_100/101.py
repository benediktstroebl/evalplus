```python
def make_a_pile(n):
    # Create a list to store the number of stones in each level
    pile = [0] * (n + 1)
    
    # Define the number of stones in the first level (the number of 'n')
    pile[0] = n
    
    # Iterate through the pile to create the rest of the levels
    for l in range(1, n + 1):
        # If the level is odd, take the next odd number
        if l % 2 == 1:
            pile[l] = l + 2
        
        # If the level is even, take the next even number
        else:
            pile[l] = l + 1
    
    return pile
```

This Python script defines a self-contained function make_a_pile(n) that takes a positive integer n as input and returns a list containing the number of stones in each level of the pile. The function initializes a list pile with zero values and assigns the number n to the first level. It then iterates through each level, determining whether it is odd or even and incrementing the count accordingly. The resulting counts are stored in the pile list, which represents the number of stones in each level. In essence, the function creates a pile of stones with the specified number of levels, where each level follows the rules of increasing by 2 or 1, resulting in the list [n, n + 2, n + 4, ..., 2 * n].