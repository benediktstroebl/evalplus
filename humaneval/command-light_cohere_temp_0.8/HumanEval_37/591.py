```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x % 2 == 0)

# Test the function
test_even = [5, 6, 3, 4]
print(sort_even(test_even))  # Expected output: [3, 6, 5, 4]
```