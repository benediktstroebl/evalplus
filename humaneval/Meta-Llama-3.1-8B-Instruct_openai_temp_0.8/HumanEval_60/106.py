### Sum of Numbers from 1 to n in Python
```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the number range.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    # Initialize a variable to store the sum
    total = 0
    
    # Use a for loop to iterate over the range from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Add each number in the range to the total
        total += i
    
    # Return the total sum
    return total

# Test cases
print(sum_to_n(30))   # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

Alternatively, you can use the formula for the sum of an arithmetic series to create a more efficient function:

```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the number range.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    # The sum of numbers from 1 to n is equal to n * (n + 1) / 2
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))   # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

This version of the function uses integer division (//) to prevent potential integer overflow issues when working with large values of n.