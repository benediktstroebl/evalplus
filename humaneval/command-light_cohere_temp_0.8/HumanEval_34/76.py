```python
def unique(lst):
    return sorted(set(lst), key=str)

# Test cases
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_unique) == [0, 2, 3, 5, 9, 123]

test_list = [5, 3, 9, 2, 8, 3, 1, 7, 0]
assert list(unique(test_list)) == [2, 3, 8, 1, 7]

test_string = "hello world"
assert unique(test_string) == ["h", "ello"]

test_set = {5, 3, 9, 2, 8, 3, 1, 7, 0}
assert set(unique(test_set)) == {2, 3, 8, 1, 7}
```
The unique function in this version is self-contained and addresses the requirements of the prompt. It accepts a unique elements in a list, sorts them in ascending order, and then produces a set of distinct elements. The test cases that follow, providing validation for the unique function.