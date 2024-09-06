```python
def make_a_pile(n):
    # Create a list to store the pile sizes
    pile = [n]
    
    # Loop to create additional pile sizes based on the given rule
    while len(pile) < (1 + n): 
        if len(pile) % 2 == 0: 
            pile.append(pile[-1] + 2)
        else: 
            pile.append(pile[-1] + 1)
    
    return pile
```

This script defines a function, `make_a_pile(n)`, that takes a positive integer `n` as input and returns a list of stone sizes for each level of the pile, adhering to the problem's rules. It starts with `n` stones in the first level, and for each subsequent level, it adds 2 stones (for even-numbered levels) or 1 stone (for odd-numbered levels) to the previous level's count. The loop continues until the pile has `1 + n` levels, ensuring a complete pile is constructed.