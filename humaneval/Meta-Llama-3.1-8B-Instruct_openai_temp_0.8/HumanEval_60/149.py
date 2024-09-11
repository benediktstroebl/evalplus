```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    # Initialize the sum variable to 0
    total_sum = 0
    
    # Loop through numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Add each number to the sum
        total_sum += i
        
    # Return the calculated sum
    return total_sum

# Test the function with provided examples
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

However, the above solution is not efficient as it has a time complexity of O(n). If you want to solve this problem more efficiently, you can use the formula for the sum of an arithmetic series:

### Arithmetic Series Formula

The sum of the first n natural numbers can be calculated using the formula:

`sum = (n * (n + 1)) / 2`

Here's how you can implement this formula in Python:

```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    # Use the arithmetic series formula to calculate the sum
    total_sum = (n * (n + 1)) // 2
    
    # Return the calculated sum
    return total_sum

# Test the function with provided examples
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

This version of the function has a time complexity of O(1), making it much more efficient for large values of n.