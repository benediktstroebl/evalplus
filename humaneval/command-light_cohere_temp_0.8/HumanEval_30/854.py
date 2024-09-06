```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

#Test cases
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive(input_list1) == [5, 3, 2, 3, 9, 123, 1]

input_list2 = [5, 3, -5, 2, -3, 3, -123]
assert get_positive(input_list2) == []

input_list3 = [-1, 2, -4, 5, 6]
assert get_positive(input_list3) == [2, 5, 6]
```
The function get_positive takes an input list and returns a new list containing only the positive numbers from the input. This is tested by passing the result to the test cases and asserting that the output list is correct.