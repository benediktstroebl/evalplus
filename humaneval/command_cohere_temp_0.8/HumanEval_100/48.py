```python
def make_a_pile(n):
    piles = []
    for i in range(n):
        if i % 2 == 1:
            piles.append(i + 3)
        else:
            piles.append(i + 4)
    return piles
```
This script defines a function `make_a_pile` that takes a positive integer `n` as input and returns a list of stone counts for each level of the pile, ensuring that each level has one more stone than the previous level.