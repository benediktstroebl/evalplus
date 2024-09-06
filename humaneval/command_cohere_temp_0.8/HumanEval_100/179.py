```python
def make_a_pile(n):
    piles = []
    for i in range(n):
        if i % 2 == 0 and len(piles) % 2 == 1:
            piles.append(n + i + 1)
        elif i % 2 != 0 and len(piles) % 2 == 0:
            piles.append(n + i + 2)
        else:
            piles.append(n + i + 3)
    return piles
```

This Python script defines a self-contained `make_a_pile` function, designed to address the problem statement. The function takes a single argument, `n`, representing the number of stones in the first level of the pile. It creates a list called `piles` to store the number of stones in each level. Using a loop that iterates up to `n` (the number of piles), the function calculates the number of stones for each subsequent level based on the parity of both the current index `i` and the length of the `piles` list. If the index is even and the list length is odd, it appends the next odd number to `piles`. If the index is odd and the list length is even, it appends the next even number to `piles`. In all other cases, it appends the next odd number plus 2 to `piles`. This logic ensures that the pile grows alternately by adding an odd or even number of stones at each level. Finally, the function returns the `piles` list, which represents the number of stones in each level of the pile.