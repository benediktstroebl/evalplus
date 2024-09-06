```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, Ellipsis]]

# Test cases
test_unique = []
test_unique.py += [range(1, 10)
test_unique += [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_unique += [None, '123']
test_unique += [Ellipsis]
test_unique += [123, Ellipsis]

for item in test_unique:
    assert unique(item) == list(set(item)) == [0, 2, 3, 5, 9, '123']
``` 
The provided code defines a function unique that takes a list as an argument and returns a new list containing the unique elements from the original list. The function uses a `seen = set()` to keep track of elements encountered so far, then iterates through the original list, adding elements to `seen` if they are not duplicates and not in [-None, Ellipsis] (which are considered as "special" elements in sets).

The test cases section follows, providing a list of items to test with the unique function. The `assert` statement is then used to check if the result of calling unique on each item is correct, comparing it with the expected set of unique elements.