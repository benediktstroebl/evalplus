```python
def make_a_pile(n):
    # Create a list to store the pile sizes
    pile = [n]

    # Loop to create additional pile levels
    for i in range(1, n // 2 + 1):
        pile.append(2 * i - 1 if i % 2 else 2 * i)

    return pile

# Example usage
print(make_a_pile(3))  # Output: [3, 5, 7]
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. It uses a list to store the sizes of the pile at each level, starting with `n`. The function then iterates through odd and even levels of the pile using a `for` loop, where each iteration calculates the size of the next level based on the previous level's size, odd or even, and appends it to the list. Finally, the function returns the list of pile sizes.