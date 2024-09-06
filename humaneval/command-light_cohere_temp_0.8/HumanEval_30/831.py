```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

#Test case 1
test_case_1 = [1, 2, -4, 5, 6]
test_result_1 = get_positive(test_case_1)
assert test_case_1 == test_result_1

#Test case 2
test_case_2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, -10]
test_result_2 = get_positive(test_case_2)
assert test_case_2 == test_result_2

#Test case 3 (Negative list)
test_case_3 = [-1, 2, -4, 5, 6]
test_result_3 = get_positive(test_case_3)
assert test_case_3 == test_result_3
``` 
This Python script defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The script also includes a test suite with three test cases to verify the correctness of the `get_positive` function.