```markdown
### Solution to the Problem

Below is a Python function that checks if all numbers in a given list `l` are below a certain threshold `t`.

```python
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    # Use the built-in all() function in combination with a generator expression
    # to check if all numbers in the list are below the threshold
    return all(num < t for num in l)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

This script defines a function `below_threshold` that takes a list `l` and an integer `t` as input. It uses a generator expression to generate a sequence of boolean values indicating whether each number in `l` is below `t`. The `all` function then checks if all of these values are True, and returns the result.

In the example usage section, we demonstrate how to use the `below_threshold` function by calling it with different input values and printing the results.