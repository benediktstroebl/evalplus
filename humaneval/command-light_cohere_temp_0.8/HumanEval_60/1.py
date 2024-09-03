```python
def sum_to_n(n: int):
    """Sums numbers from 1 to n."""
    return sum(range(1, n + 1))

# Testing the function
def test_sum_to_n():
    assert sum_to_n(30) == 465  # Expected output: 465
    assert sum_to_n(100) == 5050  # Expected output: 5050
    assert sum_to_n(5) == 15    # Expected output: 15
    assert sum_to_n(10) == 55    # Expected output: 55
    assert sum_to_n(1) == 1     # Expected output: 1

# Run the function and tests
if __name__ == "__main__":
    test_sum_to_n()
    sum_to_n(16)  # Testing the function with an invalid argument
```
The code defines a function `sum_to_n` that sums numbers from 1 to a given integer `n`. The function is then tested with various inputs using the `assert_sum_to_n` test. The code passes all tests and the `sum_to_n` function can be used as expected.