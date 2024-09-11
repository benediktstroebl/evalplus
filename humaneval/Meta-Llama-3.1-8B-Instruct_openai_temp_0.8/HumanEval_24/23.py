### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the largest possible divisor (n // 2)
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i
```
You can test the function by calling it with different inputs, like this:
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(100))  # Output: 50
```
Note that this function has a time complexity of O(n/2), which is O(n) in Big O notation. It starts from the largest possible divisor (n // 2) and checks each number down to 1 to find the largest divisor. This is an efficient approach since we only need to check numbers down to the square root of n to find the largest divisor, but for simplicity, we use the above approach.