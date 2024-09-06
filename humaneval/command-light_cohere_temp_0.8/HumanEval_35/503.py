```python
def max_element(lst):
    if not_is_sequence(lst):
        return max(lst)
    else:
        raise TypeError("Input should be a sequence")

def test_max_element():
    try:
        result = max_element([1, 2, 3])
        print("Maximum element:", result)
    except TypeError as e:
        print("Error:", str(e))
    return_result()

return_result()
```

The code defines a function max_element that calculates and returns the maximum element in a sequence. It employs a sequence interface for lists and raises a TypeError if the input is not a sequence. The code also includes a separate function test_max_element that tests the max_element function using a list of values. Finally, the test_max_element function is called to verify that the max_element function correctly identifies the maximum element in the input list.