```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The number up to which the sum is calculated.

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
    
    # Use a for loop to iterate over the numbers from 1 to n
    for num in range(1, n + 1):
        # Add each number to the total sum
        total_sum += num
    
    # Return the total sum
    return total_sum

# Test the function with the provided examples
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

However, a more Pythonic way to solve this problem would be to use the formula for the sum of an arithmetic series: `n * (n + 1) / 2`. Here is the updated code:

```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The number up to which the sum is calculated.

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
    # Calculate the sum using the formula
    return n * (n + 1) // 2

# Test the function with the provided examples
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

This version of the function is more efficient and easier to read. It directly calculates the sum without needing a loop or any additional variables.