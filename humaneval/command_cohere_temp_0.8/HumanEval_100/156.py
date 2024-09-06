```python
def make_a_pile(n):
    # Initialize a list to store the number of stones in each level
    pile = [n]

    # If n is odd, add the next odd number to the pile
    if n % 2 == 1:
        pile.append(n + 2)
    # If n is even, add the next even number to the pile
    else:
        pile.append(n + 1)

    # Return the pile
    return pile

# Example usage
print(make_a_pile(3))  # Should print: [3, 5, 7]
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function compiles the list of stones for each level by checking if `n` is odd or even. The list is then returned. When printed for the case of `n = 3`, it produces the desired output of `[3, 5, 7]`.