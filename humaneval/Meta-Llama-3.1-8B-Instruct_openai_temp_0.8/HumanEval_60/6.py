### Sum of Numbers from 1 to n
#### Problem Statement
Sum numbers from 1 to n.

#### Solution

```python
def sum_to_n(n: int) -> int:
    """
    This function sums numbers from 1 to n.

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
    # Initialize the sum to 0
    total_sum = 0
    
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Add each number to the sum
        total_sum += i
    
    # Return the final sum
    return total_sum
```

#### Explanation
This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses a simple loop to iterate over the numbers and calculate the sum.

#### Example Use Cases
```python
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```