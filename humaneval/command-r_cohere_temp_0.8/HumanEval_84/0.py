```python
def solve(N):
    """Returns the sum of digits of N in binary.

    Args:
        N (int): A positive integer.

    Returns:
        str: Sum of digits in binary.
    """
    sum_of_digits = sum(int(x) for x in str(N))
    return bin(sum_of_digits)[2:]
```