```python
def max_element(lst):
    if not_unique(lst):  # Check for empty or non-unique list
        raise ValueError("Input list must be non-empty and unique")
    return max(lst)

def test_max_element():
    try:
        result = max_element([1, 2, 3])
        print("Maximum element:", result)
    except ValueError as e:
        print("Error:", str(e))

# Test cases
test_max_element()
```
The function `max_element` takes a list `lst` as input and returns the maximum element in the list. The function first checks if the list is empty or not unique, and if it is, it raises a `ValueError`. It then uses the `max` function from the Python standard library to find the maximum element in the list. Finally, it returns the maximum element.