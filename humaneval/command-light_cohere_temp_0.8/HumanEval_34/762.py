```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
return result

# Tests
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

test_unique()
 ```
This function named unique takes an input list lst and returns a list of unique elements in sorted order. The function utilizes the array comprehension and a set to quickly identify and add unique elements to the result list.