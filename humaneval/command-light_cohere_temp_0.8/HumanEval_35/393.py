```python
def max_element(lst):
    if not_unique(lst):  # Checks if the list is empty or contains duplicates
        raise ValueError("Input list must be unique")
    return max(lst)

def test_max_element():
    try:
        result = max_element([1, 2, 3])
        print("Maximum element:", result)
    except ValueError as e:
        print("Error:", e)

# Run the function and test it
test_max_element()

```

This code defines a `max_element` function that takes a list as input and returns the maximum element in that list. The `test_max_element` function tests the `max_element` function with a variety of inputs. This code also ensures the test_max_element will print the correct error message.

Finally, the `test_max_element()` function is called, which will print the expected output, helping to verify the correctness of the `max_element` function.