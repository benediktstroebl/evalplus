```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result

# unit tests
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([10, 10]) == []
assert unique([21, 22]) == [21]
```
This code defines a function unique that takes a list lst as input and returns a new list with unique elements from lst. It uses a unique elements to filter out duplicates and return the sorted unique elements. The code also provides several unit tests to ensure the correctness of the unique function.