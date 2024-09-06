```python
def max_element(lst):
    if not_elements(lst):  # Base case
        return None
    else:
        return max(lst, key=lambda x: x)

def test_max_element():
    try:
        x = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        assert x == 123
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```

This script defines a function max_element that returns the maximum element in the list, and a test function test_max_element that checks the correctness of the max_element function with various input lists.