```python
def make_a_pile(n):
    # Calculate the number of stones in each level
    pile = [n]
    while len(pile) < n + 1:
        if n % 2 == 1:
            n += 2
        else:
            n += 1
        pile.append(n)
    return pile
```

This function uses a simple iterative approach to calculate the stones in each level based on the given odd/even condition. The `pile` is initialized with `n` stones and iteratively builds up until it reaches the desired length of `(n+1)` stones. At each iteration, it increments the `n` value by 2 if it's currently odd, and by 1 if it's even, and appends this updated value to the `pile`.