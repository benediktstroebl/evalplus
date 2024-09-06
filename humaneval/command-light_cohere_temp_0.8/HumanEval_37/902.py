```python
def sort_even(lst):
    return lst[:]

# Test cases for the function
test_sort_even = []
test_sort_even.add([1, 2, 3])
test_sort_even.add([5, 6, 3, 4])
test_sort_even.add([7, 8, 7, 9])

# Function to verify the function
def verify_sort_even(func, test):
    func(test)
    assert all(test == func(test))

# Call the function to verify the test cases
verify_sort_even(sort_even, test_sort_even)
```