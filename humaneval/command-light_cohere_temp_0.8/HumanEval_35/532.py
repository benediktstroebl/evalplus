```python
def max_element(lst):
    if not_unique(lst):  # Check for empty list or list with duplicates
        raise ValueError("Input list must be non-empty and contain unique elements")
    return max(lst)  # Use Python's built-in max() function

def test_max_element():
    try:
        print(max_element([1, 2, 3]))  # Should print 3
        print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Should print 123
    except ValueError as e:
        print("Error:", str(e))

# Run the function and test it
test_max_element()
```
This script defines a function `max_element` that takes a list as input and returns the maximum element in the list. It also includes a test function that attempts to run the `max_element` function with a variety of test lists, and handles exceptions appropriately.