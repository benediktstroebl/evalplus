```python
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

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

# Test cases
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

In this script, we define a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The `sum` function in Python calculates the sum of all elements in an iterable. The `range` function generates a sequence of numbers from 1 to `n-1` (since the upper limit is exclusive), and we add 1 to `n` in the `range` function to include `n` in the sum. We then test the function with some example inputs.