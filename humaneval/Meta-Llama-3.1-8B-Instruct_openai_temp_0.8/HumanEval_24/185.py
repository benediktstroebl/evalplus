### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n
    """
    def is_divisor(num: int) -> bool:
        """ Helper function to check if a number is a divisor of n """
        return n % num == 0

    # Start checking from n-1 downwards
    for i in range(n-1, 0, -1):
        if is_divisor(i):
            return i

    # If no divisor is found, return 1 (1 is a divisor of every number)
    return 1

# Example usage
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(10))  # Expected output: 5
print(largest_divisor(7))   # Expected output: 1
```
This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. It uses a helper function `is_divisor(num)` to check if a number is a divisor of `n`. The main function starts checking from `n-1` downwards, and returns the first number that is a divisor of `n`. If no divisor is found, it returns 1 (1 is a divisor of every number).