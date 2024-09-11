```python
# sum_to_n.py

def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
        n (int): The last number in the sequence to be summed.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    # This is more efficient than using a loop to calculate the sum
    return n * (n + 1) // 2


if __name__ == "__main__":
    # Test the function with some examples
    print(sum_to_n(30))  # Expected output: 465
    print(sum_to_n(100))  # Expected output: 5050
    print(sum_to_n(5))  # Expected output: 15
    print(sum_to_n(10))  # Expected output: 55
    print(sum_to_n(1))  # Expected output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula for the sum of an arithmetic series, which is `n * (n + 1) / 2`. This approach is more efficient than using a loop to calculate the sum. The script also includes some test cases to demonstrate the function's correctness.