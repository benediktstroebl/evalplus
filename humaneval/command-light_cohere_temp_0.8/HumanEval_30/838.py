```python
def get_positive(input_list):
    return [num for num in input_list if num > 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([5, 3, -5, 2, -3, 3, -1, 9, 0, 123]) == [1]
assert not get_positive([-.1, .2, .3, .4, .5]) == []
```
This code defines a function get_positive that takes a list of numbers as input and returns a new list containing only the positive numbers from the original list. The test cases demonstrate the