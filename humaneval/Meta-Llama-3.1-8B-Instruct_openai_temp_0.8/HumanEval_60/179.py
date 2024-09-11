### Sum of Numbers from 1 to n
#### Problem Statement
The `sum_to_n` function calculates the sum of numbers from 1 to n.

#### Solution
```python
def sum_to_n(n: int) -> int:
    """
    Sum of numbers from 1 to n.

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
    # The formula for sum of first n natural numbers is n*(n+1)/2
    return n * (n + 1) // 2
```

#### Explanation
The `sum_to_n` function uses the mathematical formula for calculating the sum of the first n natural numbers, which is n*(n+1)/2. However, since we are dealing with integers, we use the floor division operator `//` to get the integer part of the result. This ensures that the function returns an integer even for large values of n.

You can test the function with different inputs to see its output.

### Example Usage
```python
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```