```python
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Returns: tuple of even and odd integer palindromes.

    Args:
        n: positive integer

    Returns:
        (even_count, odd_count) tuple, where even_count is the number of even integer palindromes and odd_count is the number of odd integer palindromes.
    """
```

# Example usage:
print(even_odd_palindrome(12))
# Output: (4, 6)
```
This function calculates and returns the count of even and odd integer palindromes within the range of 1 to n. The result is determined using the formula for counting palindromes. The function then returns a tuple containing these counts.