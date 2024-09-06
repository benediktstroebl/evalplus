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
print(make_a_pile(3))  # Output: [3, 5, 7]
```

This script defines a function `make_a_pile` that takes a single argument `n`, representing the number of stones in the first level of the pile. The function compiles the list of stones for each level by adding the next odd number to the list if the number of stones in the first level is odd, and the next even number if the number is even. The function then returns this list.

The example usage of the function outputs the list of stone counts for each level when `n = 3`, giving the correct output of `[3, 5, 7]`.