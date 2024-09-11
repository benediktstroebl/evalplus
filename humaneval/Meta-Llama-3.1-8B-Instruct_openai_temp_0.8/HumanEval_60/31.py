### Sum of Numbers from 1 to n

Below is a Python script that implements the `sum_to_n` function.

```python
def sum_to_n(n: int):
    """
    This function sums numbers from 1 to n.
    
    Args:
    n (int): The upper limit for summing numbers.
    
    Returns:
    int: The sum of numbers from 1 to n.
    """
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

# Test the function
if __name__ == "__main__":
    print(sum_to_n(30))  # Expected output: 465
    print(sum_to_n(100))  # Expected output: 5050
    print(sum_to_n(5))    # Expected output: 15
    print(sum_to_n(10))   # Expected output: 55
    print(sum_to_n(1))    # Expected output: 1
```

Alternatively, you can use the mathematical formula for the sum of an arithmetic series: `n * (n + 1) / 2`, which provides a more efficient solution.

```python
def sum_to_n(n: int):
    """
    This function sums numbers from 1 to n using the formula for the sum of an arithmetic series.
    
    Args:
    n (int): The upper limit for summing numbers.
    
    Returns:
    int: The sum of numbers from 1 to n.
    """
    return n * (n + 1) // 2

# Test the function
if __name__ == "__main__":
    print(sum_to_n(30))  # Expected output: 465
    print(sum_to_n(100))  # Expected output: 5050
    print(sum_to_n(5))    # Expected output: 15
    print(sum_to_n(10))   # Expected output: 55
    print(sum_to_n(1))    # Expected output: 1
```