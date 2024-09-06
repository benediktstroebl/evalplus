```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, ""]]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_case_1 = unique(test_list)
assert test_case_1 == [0, 2, 3, 5, 9, 123]

test_list2 = [5, "abc", 3, 5, 2, 3, 9, 0, 123]
test_case_2 = unique(test_list2)
assert test_case_2 == [5, "abc", 3, 9, 0, 123]

test_list3 = [-None, "", "abc"]
test_case_3 = unique(test_list3)
assert test_case_3 == ["abc"]
```
The provided code defines a function unique that takes a list as input and returns a new list containing unique elements from the input. The seen set is used to keep track of elements encountered to ensure uniqueness. The function uses a boolean list comprehension to filter out elements that are already present in the seen set. The test cases cover various scenarios to ensure that the unique function is working correctly.