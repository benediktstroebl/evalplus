```python
def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]

    # Iterate through odd and even levels, adjusting n accordingly
    while n != 1:
        if n % 2 == 1:
            n = n + 2
        else:
            n = n + 1

        # Append the updated number of stones for the level to the pile
        pile.append(n)

    return pile

# Example usage
print(make_a_pile(3))  # Should print: [3, 5, 7]
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. It then iterates through odd and even levels of the pile, calculating the number of stones in each level based on the given rule and appends them to a list `pile`. Finally, it returns `pile`, which represents the number of stones in each level of the pile.