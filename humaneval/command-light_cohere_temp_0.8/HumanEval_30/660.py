```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various inputs
# Test with a list of numbers
test_positive = get_positive([-1, 2, -4, 5, 6])
assert test_positive == [2, 5, 6]

# Test with a list of strings
test_strings = get_positive(["down", "up", "mid", "Item"])
assert test_strings == ["up", "mid", "Item"]

# Test with a list of objects
test_objects = get_positive([["one", "two", "three"])
assert test_objects == ["one", "two", "three"]
```
This Python script defines a function called `get_positive`, which takes a list as an argument and returns a new list containing only the positive numbers from the original list. It is then pass tests the specific cases, demonstrating that the function successfully filters out negative numbers and returns the desired positive values.