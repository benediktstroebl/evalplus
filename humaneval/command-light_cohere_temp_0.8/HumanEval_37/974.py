```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    return even[:]

# Test the function
print(sort_even([1, 2, 3, 4, 5, 6]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))    # Expected output: [3, 6, 5, 4]
```