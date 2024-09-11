```python
# sum_to_n.py

def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

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
    # Initialize the sum variable to 0
    total_sum = 0
    
    # Loop from 1 to n (inclusive) and add each number to the sum
    for i in range(1, n + 1):
        total_sum += i
    
    # Return the calculated sum
    return total_sum

# Test the function with some examples
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

However, if you're looking for a more concise solution, you can use the formula for the sum of an arithmetic series:

```python
# sum_to_n.py

def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

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
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    return n * (n + 1) // 2

# Test the function with some examples
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```