```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test case 1
test_1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_res_1 = get_positive(test_1)
assert test_res_1 == [5, 3, 2, 3, 9, 123, 1]

#Test case 2
test_2 = [5, 3, -4, -1, 100, -5, -3, TRUE, FALSE, NULL]
test_res_2 = get_positive(test_2)
assert test_res_2 == [5, 3, -1, 100, -5, -3]

#Test case 3
test_3 = [-, -1, -5, -3, -2, -4, TRUE, -6]
test_res_3 = get_positive(test_3)
assert test_res_3 == [-, -1, -5, -3, -2, -4]
```
The function get_positive returns a list of only positive numbers in the input list. 

This function is self-contained, and its purpose is to solve the problem of getting a list of positive numbers.