```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.

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
    return (n * (n + 1)) // 2


# Test cases
if __name__ == "__main__":
    test_cases = [
        (30, 465),
        (100, 5050),
        (5, 15),
        (10, 55),
        (1, 1)
    ]

    for n, expected_sum in test_cases:
        calculated_sum = sum_to_n(n)
        assert calculated_sum == expected_sum, f"Expected sum_to_n({n}) to return {expected_sum}, but got {calculated_sum}"
```

This Python script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula `n * (n + 1) / 2`. It then includes test cases to verify the correctness of the function. If the function is correct, the script will run without errors. If the function is incorrect, it will raise an `AssertionError` with a message describing the mismatch between the expected and calculated results.