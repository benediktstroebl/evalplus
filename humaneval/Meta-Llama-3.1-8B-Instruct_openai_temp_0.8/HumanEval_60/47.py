### Sum of Numbers from 1 to n
#### Problem Description
This script calculates the sum of numbers from 1 to n.

#### Code
```python
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
    return sum(range(1, n + 1))

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

#### Explanation
This script uses Python's built-in `sum` function in combination with the `range` function to calculate the sum of numbers from 1 to n. The `range` function generates a sequence of numbers starting from 1 up to but not including n + 1, allowing us to use the `sum` function to add all these numbers together.