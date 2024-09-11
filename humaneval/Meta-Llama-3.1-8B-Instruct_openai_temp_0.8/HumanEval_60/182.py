```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the range of numbers to be summed.

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
    # Initialize a variable to store the sum
    total_sum = 0
    # Iterate over the range from 1 to n (inclusive) and add each number to the sum
    for i in range(1, n + 1):
        total_sum += i
    # Return the calculated sum
    return total_sum

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

However, this can be achieved more efficiently using the mathematical formula for the sum of an arithmetic series: 

```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n using the formula for the sum of an arithmetic series.

    Args:
    n (int): The upper limit of the range of numbers to be summed.

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
    # The formula for the sum of an arithmetic series is n * (n + 1) / 2
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This version of the function has a time complexity of O(1) and does not need to iterate over the range of numbers. It is therefore more efficient than the previous implementation.