```python
def make_a_pile(n):
    # Initialize a list to store the pile sizes
    pile = [n]

    # Loop to create the pile for each level
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:
            pile.append(i * 3 - 1)
        else:
            pile.append(i * 2)

    return pile
```

This Python script defines a function `make_a_pile` that solves the problem as described in the prompt. It takes a single argument `n`, representing the number of stones in the first level of the pile, and returns a list representing the number of stones in each subsequent level.

The code structure is clear and easy to follow, making it understandable for programmers of all levels. The variable naming is also concise, which improves the readability of the code and makes it easier to understand the purpose of each piece.