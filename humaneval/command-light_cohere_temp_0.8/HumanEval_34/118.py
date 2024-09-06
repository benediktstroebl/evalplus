```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not float('inf')]

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert set(unique(test_case2)) == {1, 2, 3, 4, 5, 6, 7, 8}

# Test case 3
test_case3 = [5, 3, "abc", 123, "def"]
assert set(unique(test_case3)) == {"abc", 123, "def"}
```
The above Python script defines a function unique that takes a list as input and returns a list of unique elements from the input list, along with any float values. The function utilizes a basic set data to track seen elements, then iterates through the input list and returns elements that are not in the set and not float('inf'). The test suite includes three test cases, which verify that the unique function correctly returns the expected output for various input lists.