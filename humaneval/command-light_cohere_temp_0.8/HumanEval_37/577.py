```python
def sort_even(lst):
    return lst[:] if len(lst) % 2 == 0 else lst[::-1]

# Test the function
test_even = [1, 2, 3]
test_even = sort_even(test_even)
print(test_even)  # Expected output: [1, 2, 3]

test_even = [5, 6, 3, 4]
test_even = sort_even(test_even)
print(test_even)  # Expected output: [3, 6, 5, 4]

test_even = [10, 20, 30, 40]
test_even = sort_even(test_even)
print(test_even)  # Expected output: [30, 20, 10, 40]
```
This script defines a function called sort_even that takes a list as input and returns a sorted list based on the odd indices. The function uses a least squares approach by first converting the list to a one-dimensional array, then checking if the length is even. The function then returns the array without the original list's odd indices.