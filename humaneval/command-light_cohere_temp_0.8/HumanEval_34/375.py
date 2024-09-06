```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not  set()]

# Test the function with a sample list
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_list) == [0, 2, 3, 5, 9, 123], "Function returned unexpected result"

# Test with empty list
assert unique([]) == [], "Function didn't handle empty list correctly"

# Test with list of strings
assert unique(["a", "b", "c"]) == ["a", "b", "c"], "Function returned unexpected result"

# Test with list of integers
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Function returned unexpected result"
```
The above script provides a function unique that takes in a list and returns all the unique elements from that list. It is also includes many test cases to validate the correctness of the function.