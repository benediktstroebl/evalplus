```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

#Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_list) == [0, 2, 3, 5, 9, 123]

#Test empty list
assert unique([]) == []

#Test list with duplicate values
test_list = [1, 2, 3, 4, 5, 6, 7]
assert unique(test_list) == [1, 2, 3, 4, 5]

#Test list of strings
test_list = ["a", "b", "c", "a"]
assert unique(test_list) == ["a", "b", "c"]
 ```

This script defines a function unique that takes a list lst as input and returns a new list with unique elements from the original. The function uses a set seen to keep track of elements that have been seen, then it iterates through the original list and adds elements to the set if they are not in the seen set and not 0. The test cases that include an empty list, a list with duplicates, and a list of strings, and they are used to verify that the unique function works correctly.