```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    sum = n * (n + 1) // 2
    
    return sum

# Example use cases
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1

    try:
        print(sum_to_n(-1))  # Should raise a ValueError
    except ValueError as e:
        print(e)  # Output: n must be a non-negative integer
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula for the sum of an arithmetic series: `n * (n + 1) / 2`. The script also includes example use cases and error handling to ensure that `n` is a non-negative integer.