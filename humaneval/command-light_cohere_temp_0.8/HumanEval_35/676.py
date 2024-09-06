```python
def max_element(lst):
    return max(lst)

# Test the function with a list of numbers
test_max_element = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_max_element) == 123

# Test the function with a list of strings
test_str_element = ["h", "e", "l", "l", "o"]
assert max_element(test_str_element) == "l"
```
This Python code defines a function `max_element` that returns the maximum element from a given list. The function is then tested using two different lists of elements: one with numeric values and the other with string characters. The test assertions verify that expected results of the `max_element` function.