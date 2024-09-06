```python
def make_a_pile(n):
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```
This Python script defines a function called `make_a_pile` that takes a single argument `n`, representing the number of stones needed at the base of the pile. The function constructs a list (`pile`) where each element represents the number of stones in each level of the pile. It starts with `n` stones in the first level and enters a loop that iteratively calculates the number of stones for the next level until the total number of levels matches the specified number `n+1`.

The logic within the loop is where the odd/even differentiation occurs. If the current `n` is odd, it adds 2 to the next level, making it odd. If `n` is even, it increments by 1 to produce an even number for the next level. This process continues until the pile reaches the desired size, and the resultant `pile` list captures the count of stones for each level.