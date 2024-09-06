```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 0:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This script defines a function `make_a_pile` that takes a positive integer `n` as input and returns a list of stone counts for each level of the pile. It starts with `n` stones on the first level, and then continues by incrementing the count by 2 (or 1) depending on whether `n` was even or odd, thereby creating a series of increasingly uneven numbers that mimic the growth of a pyramid's base. The loop continues until the pile has `n+1` levels, ensuring that the final list has the correct number of elements.