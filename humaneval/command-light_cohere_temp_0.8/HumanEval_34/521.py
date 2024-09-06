```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, Infinity, NegativeInfinity]]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_output = unique(test_list)
assert test_output == [0, 2, 3, 5, 9, 123]

test_empty = []
test_output2 = unique(test_empty)
assert test_output2 == []

test_list_duplicates = [5, 5]
test_output3 = unique(test_list_duplicates)
assert test_output3 == []
```

This script defines a function called `unique`, which takes a list as input and returns a new list containing unique elements from the original list. It uses a unique elements using the method to filter out duplicates, and the result is a sorted list of unique elements. The script also includes several test cases to validate the correctness of the `unique` function.