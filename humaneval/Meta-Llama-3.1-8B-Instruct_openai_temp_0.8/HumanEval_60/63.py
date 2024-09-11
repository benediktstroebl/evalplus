```python
# sum_to_n.py

def sum_to_n(n: int):
    """
    This function calculates the sum of all numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of all numbers from 1 to n.

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
    # Using the formula for the sum of an arithmetic series
    # n*(n+1)/2 is the sum of all numbers from 1 to n
    return n * (n + 1) // 2


# Testing the function
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1
```

This script uses the formula for the sum of an arithmetic series, `n*(n+1)/2`, to efficiently calculate the sum of all numbers from 1 to `n`. This approach has a time complexity of O(1), making it much faster than a naive approach that sums the numbers one by one.