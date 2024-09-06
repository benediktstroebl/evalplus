```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float]

# Test the function with various types of lists
test_unique_passes = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [5, 5],
    [5, 2, 3, 5],
    [{"a": 1}, 5, "a"],
    [1, 2, 3, [1]]
]

for test_list in test_unique_passes:
    assert unique(test_list) == set(test_list)
``` 
This function uses the set data structure to keep track of unique elements in the input list, and then filters out duplicates.  It list comprehension is efficient way to extract unique elements from a list while avoiding duplicates in the process.