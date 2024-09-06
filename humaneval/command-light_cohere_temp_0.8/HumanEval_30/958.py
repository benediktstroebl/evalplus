```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with several inputs
test_positive = get_positive([-1, 2, -4, 5, 6])
test_positive(test_output)  # Test the output with the previous result
```

This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The function uses a loop to iterate through each element in the input list, and uses the condition `x >= 0` to filter out any negative elements. The final output is a list containing only positive elements from the original list.