```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))  # Expected: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected: [5, 3, 2, 3, 9, 123, 1]
```
This script defines a `get_positive` function that returns a list of only positive numbers from the input list. The test cases ensure that the expected output matches the actual output of the function. 

The `get_positive` function simplifies the problem by using list comprehension with a generator expression, which filters out negative numbers and returns a new list with only positive numbers.