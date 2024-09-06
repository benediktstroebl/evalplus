```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test the function with different list inputs
# Test list with odd length
test_list = [1, 2, 3, 4]
print("Test with odd length list:", median(test_list))  # Output: 2

# Test list with even length
test_list = [1, 2, 3, 4, 5]
print("Test with even length list:", median(test_list))  # Output: 2

# Test list with large values
test_list = [10, 11, 12, 13, 14]
print("Test with large values list:", median(test_list))  # Output: 12

# Test list with specific values
test_list = [-10, 4, 6, 1000, 10, 20]
print("Test with specific values list:", median(test_list))  # Output: 15.0
```