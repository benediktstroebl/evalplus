```python
def truncate_number(n):
    return n if n <= 1 else n // 10

# Test the function with a range of numbers
test_range = [1.5, 2.0, 2, 8.1, 0.0, 0.0, 99999, 0.1]
print(f(test_range))  # Output: [0, 2, 8, 0, 9]

# Test the function with a single number
test_single = 3
print(test_single)
print(truncate_number(test_single))  # Output: 0.5
```