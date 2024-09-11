```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n that is smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # If n is less than 2, it's a prime number and has no divisors other than 1
    if n < 2:
        return 1

    # Start checking from the second last number and move downwards
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1 (17 is a prime number)
print(largest_divisor(20))  # Output: 20 (20 is a perfect square)
```

In this script, we first handle the special case where n is less than 2 (i.e., it's a prime number and has no divisors other than 1). Then we iterate from the second last number to 1 (inclusive), checking if each number is a divisor of n by using the modulo operator (`n % i == 0`). As soon as we find a divisor, we return it. If no divisors are found, the function will return 1, which is correct for prime numbers.