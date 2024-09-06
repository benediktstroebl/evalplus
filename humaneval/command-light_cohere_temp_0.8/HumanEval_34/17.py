```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x_x)
    return result

# Tests
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

test_unique()
```
This code defines a function called unique that takes a list as input and returns a new list with unique elements from the original. The function uses a set to keep track of elements seen so far, and then iterates through the input list, adding elements to the seen set and appending them to the result list if they are not previously seen. The test function then tests the unique function with a sample input list, and asserts that the returned list contains the correct unique elements.