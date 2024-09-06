```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in []]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ['a', 'a', 'b', 'c'],
    [1, 2, 3, 4, 5, 6],
]

for test_case in test_cases:
    print(unique(test_case))
```
This code defines a function called unique that takes a list as an argument and returns a new list with unique elements. The function uses a set to keep track of the elements that have been encountered, and then it iterates through the original list and adds elements to the set if they are not present in the set and are not empty. The function then returns a set of all elements that were not added to the seen set.

The code then provides several test cases for the unique function, and prints the resulting unique lists.