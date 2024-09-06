```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ['a', 'b', 'c'],
    [1, 2, 3, 4, 5],
]

for test_case in test_cases:
    assert unique(test_case) == [0, 2, 3, 5, 9, 123]
``` 
This script defines a function `unique` that takes a list as an argument and returns a new list with the unique elements from the input. The function utilizes a set data structure to quickly identify unique elements. The function then iterates through each element in the input list and checks if the element is not in the seen set. If the element is not in the set and not None, it is added to the result list.