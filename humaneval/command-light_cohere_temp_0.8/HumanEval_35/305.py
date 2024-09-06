```python
def max_element(lst):
    if not_unique(lst):  # Check for empty list or duplicates
        raise ValueError("Input list must contain unique elements")
    return max(lst)

def test_max_element():
    try:
        x = max_element([1, 2, 3])
        print("Maximum element:", x)
    except ValueError as e:
        print("Error:", e)

# Example usage
test_max_element()
```
This code defines a `max_element` function that finds the maximum element in a list.

First, it checks whether the list is empty or contains duplicates. If the list has duplicates, it raises a `ValueError` with an appropriate error message.

The function then uses the `max` function from the `collections` module to find the maximum element in the list.

The `test_max_element` function contains a test case that creates a list, and calls the `max_element` function to find the maximum element.

Finally, an example usage is demonstrated, where the `test_max_element` function is called to check the correctness of the `max_element` function.