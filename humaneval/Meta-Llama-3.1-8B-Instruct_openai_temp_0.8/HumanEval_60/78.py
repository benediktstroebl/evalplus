```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the sum.
    
    Returns:
    int: The sum of numbers from 1 to n.
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Add each number to the total sum
        total_sum += i
        
    return total_sum

# Test the function
print(sum_to_n(30))  # Should print 465
print(sum_to_n(100))  # Should print 5050
print(sum_to_n(5))  # Should print 15
print(sum_to_n(10))  # Should print 55
print(sum_to_n(1))  # Should print 1
```

However, there is a more efficient way to calculate this sum using the formula for the sum of an arithmetic series: `n * (n + 1) / 2`.

Here's how you can implement it:

```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the sum.
    
    Returns:
    int: The sum of numbers from 1 to n.
    """
    # Use the formula for the sum of an arithmetic series
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Should print 465
print(sum_to_n(100))  # Should print 5050
print(sum_to_n(5))  # Should print 15
print(sum_to_n(10))  # Should print 55
print(sum_to_n(1))  # Should print 1
```

Both versions of the function should produce the same results, but the second version is generally faster and more memory-efficient because it doesn't require a loop.