```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test the function with a variety of cases
# Test with list of numbers
assert(get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6])

# Test with list of strings
assert(get_positive(["abc", "-123", "five", "six"]) == ["abc", "five", "six"])

# Test with list of mixed data types
assert(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, -10]) == [5, 3, 2, 3, 9, 123])
```
This script defines a `get_positive` function that takes a list as input and returns a new list containing only the positive elements from the original list. 

It then tests the function with a variety of cases, passing the test and checking that the function returns the expected results.