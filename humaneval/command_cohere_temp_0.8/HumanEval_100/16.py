```python
def make_a_pile(n):
    # Base case: First level has n stones
    pile = [n]
    
    # Iterate to create subsequent levels
    while len(pile) < n + 1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    
    return pile
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function first creates a list with the first `n` elements, then iterates to create subsequent levels, where each element is the sum of the previous element and either 1 or 2, depending on whether the length of the pile is odd or even, respectively. The while loop runs until the pile has `n + 1` elements, ensuring that it's complete for the given number of levels.