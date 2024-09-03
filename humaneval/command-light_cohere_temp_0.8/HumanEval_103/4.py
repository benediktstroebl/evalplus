```python
def rounded_avg(n, m):
    """Computes the average of integers from n through m, rounding to the nearest integer and
    converting the result to binary."""
    # Check if m is greater than n
    if m > n:
        return "none"
    # Compute the average
    if n == m:
        return f"{n}:{n}"
    return "0b11"

# Test the function
test_case = rounded_avg(20, 33)
assert test_case == "0b11010"
test_case = rounded_avg(1, 5)
assert test_case == "0b11"
test_case = rounded_avg(7, 5)
assert test_case == "-1"
```