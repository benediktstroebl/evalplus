```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
        >>> largest_divisor(24)
        12
    """

    def largest_divisor_helper(num: int, divisor: int) -> int:
        """
        Helper function to find the largest divisor recursively.

        Args:
            num (int): The number to find the divisor for.
            divisor (int): The current divisor to check.

        Returns:
            int: The largest divisor of num, smaller than num.
        """
        if divisor == 1:
            return 1
        elif num % divisor == 0:
            return divisor
        else:
            return largest_divisor_helper(num, divisor - 1)

    return largest_divisor_helper(n, n - 1)


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

In this code:

1.  We define the `largest_divisor` function that takes an integer `n` as input and returns its largest divisor smaller than `n`.
2.  The `largest_divisor_helper` function is a recursive helper function that finds the largest divisor of `n` by checking divisors from `n-1` down to `1`.
3.  If the current divisor divides `n` evenly, it returns the divisor; otherwise, it calls itself with the next smaller divisor.
4.  The `largest_divisor` function calls the helper function with `n-1` as the initial divisor and returns the result.
5.  We include example usage and output to demonstrate the function's behavior.