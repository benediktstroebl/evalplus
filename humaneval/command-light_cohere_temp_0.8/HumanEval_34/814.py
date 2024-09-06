```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not is None]

# Test cases
tests = [
    [(5, 3), (5, 2), (3, 3), (3, 5), (9, 0), (123, 0)],
    ()
]

for case in tests:
    assert unique(case) == [0, 2, 3, 5, 9, 123]
``` 
This script defines a function unique that returns a list of unique elements from the input list lst. The function uses a tested using the set and a list comprehension to filter out duplicate and None elements, then returns only the unique items. 

You can use this code as- `unique` to solve the problem.