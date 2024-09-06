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

This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function aims to generate a list representing the number of stones in each level of the pile, where the element at index `i` represents the number of stones in the (i+1)-th level.

The function uses a `for` loop to iterate through even and odd values of `i`, appending the appropriate value to the `piles` list, which represents the number of stones in the next level. Finally, the function returns the `piles` list, which provides the desired number of stones for each level of the pile.