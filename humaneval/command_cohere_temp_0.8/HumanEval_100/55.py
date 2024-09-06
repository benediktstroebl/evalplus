```python
def make_a_pile(n):
    # Create a list to store the pile sizes
    pile = [n]
    
    # Loop to create additional pile sizes based on the given rule
    for l in range(1, n + 1):
        if l % 2 == 0 and pile[-1] % 2 == 1:
            pile.append(l + 1)
        elif l % 2 != 0 and pile[-1] % 2 == 0:
            pile.append(l + 2)
        else:
            pile.append(pile[-1] + 1)
    
    return pile
```

This script defines a function, `make_a_pile(n)`, which takes a positive integer `n` as input and returns a list of stone sizes for each level of the pile, abiding by the given rules. It starts with `n` stones in the first level, and then iteratively calculates the number of stones for each subsequent level, odd or even, based on the previous level's count.