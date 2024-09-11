```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Examples:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
    """
    return sum(range(1, n + 1))


# Test the function
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1
```

In this code, we define the `sum_to_n` function, which takes an integer `n` as input and returns the sum of numbers from 1 to `n`. We use the built-in `range` function to generate a sequence of numbers from 1 to `n` and the `sum` function to calculate the sum of this sequence.

The docstring of the `sum_to_n` function includes a description of the function, its parameters, return value, and some example usage. The last part of the code is a test block that calls the `sum_to_n` function with different inputs and prints the results.