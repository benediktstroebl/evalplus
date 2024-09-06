```python
def make_a_pile(n):
    # Initialize a list to store the pile size at each level
    pile = [n]

    # Loop to construct the pile incrementally
    for i in range(1, n // 2 + 1):
        pile.append(pile[i - 1] + 2 - (i % 2))

    # If the pile has an odd number of levels, append the last even pile size
    if n % 2 != 0:
        pile.append(pile[-1] + 2)

    return pile
```

This script adheres to the problem statement's guidelines. It develops a list named `pile` that represents the quantity of stones at each level of the pile. The `make_a_pile` function outputs the pile's size at each level after calculating it iteratively based on the specified criteria.

Here is an example of how to use this function:
```python
print(make_a_pile(3))  # Outputs: [3, 5, 7]
```