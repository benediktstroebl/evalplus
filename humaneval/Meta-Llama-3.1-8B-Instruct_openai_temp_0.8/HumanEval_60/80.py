Here's a Python function that uses a simple arithmetic formula to calculate the sum of numbers from 1 to n. This method avoids using a loop or recursion, making it more efficient.

```python
def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.
    
    The formula used here is based on the formula for the sum of an arithmetic series: 
    sum = (n * (a1 + an)) / 2, where a1 is the first term and an is the last term.
    
    In this case, a1 = 1 and an = n, so the formula simplifies to: 
    sum = (n * (1 + n)) / 2
    
    Args:
        n (int): The input number up to which the sum is calculated.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    
    return (n * (n + 1)) // 2

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

This function works by directly calculating the sum using the formula for the sum of an arithmetic series, and then returning the result. The `//` operator is used for integer division to avoid float results. The function also includes input validation to ensure that the input is a positive integer. If the input is not valid, it raises a ValueError with a descriptive message.