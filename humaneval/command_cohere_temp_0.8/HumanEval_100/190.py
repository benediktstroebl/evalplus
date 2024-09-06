```python
def make_a_pile(n):
    piles = []
    for i in range(n):
        if i % 2 == 0:
            piles.append(i + 2)
        else:
            piles.append(i + 1)
    return piles
```

This script defines a function `make_a_pile` that takes a positive integer `n` as input and returns a list of stone counts for each level of the pile. The function iterates through levels from 0 to n-1, determining whether each level should have an odd or even number of stones based on the parity of the level number. It then constructs a list reflecting the required stone counts for each level, which is the output of the function.