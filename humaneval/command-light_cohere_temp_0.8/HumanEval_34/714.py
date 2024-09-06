```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not]}

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 6, 7],
    [9, 2, 5],
    ['coffee', ' coalesce', ' Clyde', ' sub'],
    [1, 2, 3],
    [20, 40, 60],
    [True, False, True]
]

for test_case in test_cases:
    print(unique(test_case))
``` 
This function unique is a Python function that takes a list as an input and returns a list of unique elements in that list, as per the problem statement. 

The function uses the set() function to create a set of unique elements in the input list, and then uses a list comprehension to filter out all elements that are in the set but also not in the input list.

This function can be easily integrated into any Python project or code base as a convenient way to solve the problem of returning unique elements from a list.