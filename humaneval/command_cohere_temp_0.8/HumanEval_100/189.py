```python
def make_a_pile(n):
    # Create a list to store the pile size at each level
    pile = [n]
    
    # Loop through odd levels
    for i in range(1, (n // 2) + 1):
        pile.append(2 * i - 1)

    # Loop through even levels
    for i in range(1, (n // 2) + 1):
        pile.append(2 * i)

    return pile
```

This approach uses two nested loops to iterate through the odd and even levels of the pile. For each level, it calculates the `next odd` or `next even` number as specified by the problem statement and adds it to the pile list. Finally, the script returns the pile list as the solution.