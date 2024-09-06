```python
def max_element(lst):
    if not_unique(lst):
        raise ValueError("Input list must contain unique elements")
    return max(lst)

def test_max_element():
    try:
        max_element([1, 2, 3])
        print("Successfully found maximum element 3")
    except ValueError as e:
        print(f"Error: {e}")
```
The function `max_element` returns the maximum element in the list. The function `test_max_element` tests the function with a sample list and verifies if the list contains unique elements.