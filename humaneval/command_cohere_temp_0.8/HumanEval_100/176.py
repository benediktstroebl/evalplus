```python
def make_a_pile(n):
    # Base case: first level has n stones
    pile = [n]
    
    # Iterate to build the pile
    while len(pile) < n + 1:
        if len(pile) % 2 == 1:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    
    return pile
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function first creates a list with the first `n` stones and then iteratively adds stones to the pile, ensuring that each level has an odd number of stones followed by an even number of stones, and vice versa. The while loop continues until the pile has `n + 1` levels. The final list `pile` contains the number of stones for each level of the pile.