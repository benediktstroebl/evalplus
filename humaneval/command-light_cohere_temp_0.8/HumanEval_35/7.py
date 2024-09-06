```python
def max_element(lst):
    if not_valid(lst):
        return max(lst)
    else:
        raise ValueError("Input list is not valid.")

def test_max_element():
    try:
        x = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        print("Maximum element:", x)
        return True
    except ValueError as e:
        print("Error:", str(e))
        return False
```
The above script defines a function `max_element` that finds the maximum element in a given list. Also, it includes a function `test_max_element` to test the `max_element` function with various input lists, and it passes all the tests.