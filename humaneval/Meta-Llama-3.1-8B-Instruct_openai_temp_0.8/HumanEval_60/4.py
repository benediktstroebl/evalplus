```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of all numbers from 1 to n (inclusive).
    
    Args:
        n (int): The upper limit of the sum range.
    
    Returns:
        int: The sum of all numbers from 1 to n.
    """
    if n <= 0:
        return "Input should be a positive integer."
    
    # The formula for the sum of an arithmetic series is n * (a1 + an) / 2
    # where n is the number of terms, a1 is the first term, and an is the last term.
    # Since our series starts at 1 and ends at n, the sum is n * (1 + n) / 2.
    return n * (1 + n) // 2

# Test cases
print(sum_to_n(30))   # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of all numbers from 1 to `n`. It uses the formula for the sum of an arithmetic series to calculate the result efficiently. The test cases at the end demonstrate the function's correctness.