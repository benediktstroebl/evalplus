```python
def sort_even(lst):
    return lst[:] if any(n % 2 == 0 for n in lst) else lst

# Test the function with sample inputs
print(sort_even([1, 2, 3, 4, 5, 6]))  # Expected output: [1, 2, 3, 4, 5]
print(sort_even([5, 6, 3, 4]))    # Expected output: [3, 6, 5, 4]
print(sort_even([10, 20, 30, 40, 50])) # Expected output: [40, 30, 50, 20, 10]
```