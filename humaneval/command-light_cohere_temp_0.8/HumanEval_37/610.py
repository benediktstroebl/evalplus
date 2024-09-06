```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even + [x for x in lst if x % 2 != 0]

# Test cases
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
print(sort_even([10, 20, 30, 40, 50]))  # Expected output: [40, 30, 20, 10]
```