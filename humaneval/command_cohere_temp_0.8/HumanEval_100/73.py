```python
def make_a_pile(n):
    # Initialize a list to store the number of stones per level
    pile = [n]

    # Loop to create additional levels according to the problem specification
    for i in range(1, n // 2 + 1):
        if i % 2 == 1:  # If the current level is odd (first or third, etc.)
            pile.append(i + 2)
        else:  # If the current level is even (second or fourth, etc.)
            pile.append(i + 1)

    return pile

# Example usage
print(make_a_pile(3))  # Should print: [3, 5, 7]
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. It returns a list where the first element is the number of stones in the first level (`n`), then the number of stones in the second level is the next odd number to `n` if `n` was odd, and the next even number if `n` was even. This pattern continues for subsequent levels until the list reaches the number of stones in the `(n // 2)` level. The list is then returned.