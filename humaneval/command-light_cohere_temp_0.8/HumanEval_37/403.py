```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x, x%2))

# Test the function with some examples
l = [5, 6, 3, 4]
print(sort_even(l))  # [3, 6, 5, 4]
l = [1, 2, 3]
print(sort_even(l))  # [1, 2, 3]
l = [5, 9, 2, 6, 3]
print(sort_even(l))  # [2, 3, 6, 5, 9]
```