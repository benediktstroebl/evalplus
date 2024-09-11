```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
    n (int): The input number up to which the sum is calculated.
    
    Returns:
    int: The sum of numbers from 1 to n.
    
    Raises:
    TypeError: If the input is not an integer.
    ValueError: If the input is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Use the Gauss's formula for sum of first n natural numbers
    # The formula is n*(n+1)/2
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))    # 15
print(sum_to_n(10))   # 55
print(sum_to_n(1))    # 1
```

This code defines the `sum_to_n` function, which takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses Gauss's formula for the sum of the first `n` natural numbers, which is `n * (n + 1) / 2`. The code also includes test cases to ensure the function is working correctly.