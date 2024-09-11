### Sum of Numbers from 1 to n
#### Problem Statement
The function `sum_to_n` calculates the sum of all integers from 1 to `n`.

#### Solution
```python
def sum_to_n(n: int) -> int:
    """
    Sum of numbers from 1 to n.

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

# Example usage:
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```
Note: The solution uses the arithmetic series formula to calculate the sum in O(1) time complexity. This is more efficient than using a loop to calculate the sum.