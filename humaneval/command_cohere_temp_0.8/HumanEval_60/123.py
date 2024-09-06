```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    Args:
        n (int): The highest number to be included in the sum.
    Returns:
        int: The sum of numbers from 1 to n.
    """
    return sum(range(1, n + 1))
```
This script defines a function `sum_to_n` taking a single argument `n` which is the upper limit of the sum. The function sums the integers from 1 to `n` using the `sum` function applied to the result of `range` which generates a sequence of numbers from the start value to the end value (inclusive). The function is aptly commented to explain its purpose and usage.