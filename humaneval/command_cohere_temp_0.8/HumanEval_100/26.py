```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if len(pile) % 2 == 0 and pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile
```
This code defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. It constructs a list `pile` where each element represents the number of stones in a respective level of the pile. Starting from the first level (`n` stones), it iteratively adds stones to the pile based on the following rules:
1. If the current level has an even number of stones (`pile[-1]` is even), the next level will have an even number of stones, so it adds 2 to the current count.
2. If the current level has an odd number of stones (`pile[-1]` is odd), the next level will have an odd number of stones, so it adds 1 to the current count.

The loop continues until `pile` contains `n+1` elements, ensuring that the pile has the correct number of levels. The function returns the `pile` list.