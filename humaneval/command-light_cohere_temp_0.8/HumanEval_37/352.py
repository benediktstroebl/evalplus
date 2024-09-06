```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x + 1)

# Test the function
test_even = [5, 6, 3, 4]
test_even_sorted = sort_even(test_even)

assert test_even_sorted == [3, 6, 5, 4]
```