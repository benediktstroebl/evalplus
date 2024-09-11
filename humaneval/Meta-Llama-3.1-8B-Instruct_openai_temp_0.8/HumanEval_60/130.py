```python
def sum_to_n(n: int):
    """
    This function calculates the sum of all numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of all numbers from 1 to n.
    """

    # Initialize the sum variable to 0
    total_sum = 0
    
    # Loop through all numbers from 1 to n (inclusive)
    for num in range(1, n + 1):
        # Add each number to the total sum
        total_sum += num
    
    # Return the total sum
    return total_sum


# Example usage:
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

Alternatively, you can use the mathematical formula for the sum of an arithmetic series to make the function more efficient:

```python
def sum_to_n(n: int):
    """
    This function calculates the sum of all numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of all numbers from 1 to n.
    """

    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    return n * (n + 1) // 2


# Example usage:
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```