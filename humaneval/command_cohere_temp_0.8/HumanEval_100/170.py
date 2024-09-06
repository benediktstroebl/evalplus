```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]
    
    # Compute the number of stones for the next level depending on the parity of n
    while n != 1:
        if n % 2 == 1:
            n = n + 2
        else:
            n = n + 1
    
        # Append the computed number of stones to the pile
        pile.append(n)
    
    return pile
```

This Python script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function returns a list where each element represents the number of stones in each level of the pile. It first starts with `n` stones in the first level, then constructs subsequent levels, alternating between increasing even and odd numbers. The condition `while n != 1` ensures that the loop continues until the last level of the pile is reached (when `n` becomes 1), thus determining the number of stones for each level appropriately.