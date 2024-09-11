```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
    n (int): The upper limit for the sum.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    return sum(range(1, n + 1))

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

In this script, we use the built-in `sum` function in Python to calculate the sum of numbers from 1 to `n`. The `range` function generates a sequence of numbers from 1 to `n` (exclusive), and the `sum` function adds up all the numbers in this sequence. The `+ 1` in `range(1, n + 1)` is necessary because `range` is exclusive of the end value.