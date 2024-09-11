Here's the Python script that implements the `sum_to_n` function:
```markdown
# sum_to_n.py

def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

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
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```
This script uses the formula for the sum of an arithmetic series (`n * (n + 1) / 2`) to efficiently calculate the sum of numbers from 1 to `n`. This approach has a time complexity of O(1), making it much faster than the naive approach of summing numbers using a loop.

You can save this script to a file (e.g., `sum_to_n.py`) and run it using Python (e.g., `python sum_to_n.py`) to verify that the function works as expected.