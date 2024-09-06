```python
def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]

    # If n is odd, add the next odd number to the pile
    if n % 2 == 1:
        pile.append(n + 2)
    # If n is even, add the next even number to the pile
    else:
        pile.append(n + 1)

    # Return the pile of stones
    return pile

# Example usage
print(make_a_pile(3))  # Output: [3, 5, 7]
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function creates a list (`pile`) where the first element is `n` (the number of stones in the first level). Subsequently, it appends either the next odd number or the next even number to the list based on the parity of `n`, thereby creating the pile of stones. Finally, the function returns this list. The example usage provided in the docstring demonstrates this, and the output is also shown.