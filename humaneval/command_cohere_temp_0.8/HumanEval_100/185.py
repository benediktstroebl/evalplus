```python
def make_a_pile(n):
    piles = [n]
    while len(piles) < n + 1:
        if piles[-1] % 2 == 1:
            piles.append(piles[-1] + 2)
        else:
            piles.append(piles[-1] + 1)
    return piles
```
The function uses a simple iterative approach to calculate the stones in each level based on the given integer `n`. It starts with `n` stones on the first level and iteratively calculates the number of stones for the next level by adding 1 if the previous level had an odd number of stones, and 2 if the previous level had an even number of stones.