```markdown
**Sum of Numbers from 1 to n**
================================

This script provides a function `sum_to_n` to calculate the sum of numbers from 1 to `n`.

```python
def sum_to_n(n: int) -> int:
    """
    This function sums numbers from 1 to n.

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
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

**Explanation**
---------------

The function `sum_to_n` uses the formula for the sum of an arithmetic series to calculate the sum of numbers from 1 to `n`. The formula is:

`sum = n * (n + 1) / 2`

This formula is derived from the fact that the sum of an arithmetic series is equal to the average of the first and last term, multiplied by the number of terms. In this case, the average of the first and last term is `(n + 1) / 2`, and there are `n` terms.

This function runs in constant time, O(1), because it uses a simple formula to calculate the sum, rather than iterating over the numbers from 1 to `n`. This makes it much more efficient than a function that uses a loop to calculate the sum.