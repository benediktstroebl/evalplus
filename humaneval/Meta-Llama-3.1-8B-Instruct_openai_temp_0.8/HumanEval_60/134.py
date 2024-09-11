### Sum of Numbers from 1 to n
#### Problem Description
This script calculates the sum of numbers from 1 to n using a mathematical formula.

#### Code
```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    # Using the formula for the sum of an arithmetic series: n*(n+1)/2
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))   # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))    # Expected output: 15
print(sum_to_n(10))   # Expected output: 55
print(sum_to_n(1))    # Expected output: 1
```

#### Explanation
This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the mathematical formula for the sum of an arithmetic series, which is `n*(n+1)/2`. This formula is used to calculate the sum directly instead of iterating over the numbers from 1 to `n`, resulting in a more efficient solution. The script includes test cases to demonstrate the function's correctness.