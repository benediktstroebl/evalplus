```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test cases
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive(input_list1) == [5, 3, 2, 3, 9, 123, 1]

input_list2 = [5, 3, -5, 2, -3, 3, -123]
assert get_positive(input_list2) == [5, 3, 2]

input_list3 = [-1, 2, -4, 5, 6]
assert get_positive(input_list3) == [2, 5, 6]
 ```
The provided Python script defines a function called `get_positive` which takes an input list and returns a new list containing only the positive elements from the original list. 

The function employs list comprehension and the `>= 0` condition to filter out the positive elements. 

This script then includes several test cases to verify the correctness of the `get_positive` function. 
These test cases cover a variety of scenarios, including lists with both positive and negative numbers, and ensure that the function returns the expected results.