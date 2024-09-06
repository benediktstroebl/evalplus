```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n+1:
        if n % 2 == 1:
            n += 2
            pile.append(n)
        else:
            n += 1
            pile.append(n)
    return pile
```
This code defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. It constructs a list `pile` with the initial level of `n` stones. Using a `while` loop, it iteratively adds stones to the pile by increasing the count by 2 (for odd levels) or by 1 (for even levels), and appends the updated count to the `pile` list. This process continues until the length of the `pile` reaches `n+1`. In the end, it returns the `pile` list containing the counts of stones for each level of the pile.