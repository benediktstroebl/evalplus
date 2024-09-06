```python
def make_a_pile(n):
    # Determines the next level accordingly based on the initial value of n.
    # If n is even, the next level will have the next even number of stones.
    # If n is odd, the next level will have the next odd number of stones.
    if n % 2 == 0:
        level = n + 2
    else:
        level = n + 1
    
    # Generates the entire pile by iteratively adding 1 to the level variable.
    # Since the first level has n stones, the subsequent levels are indexed.
    return [n] + [level + i for i in range(n - 1)]
```