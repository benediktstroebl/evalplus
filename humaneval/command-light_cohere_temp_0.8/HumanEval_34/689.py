```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not in [-None, -illus]}
    
# Test cases
tests = [
    dict(zip(['5 3 5 2 3 3 9 0 123', 'abc', 'A']) 
, unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
    assert unique([5, 3, 5, 2, 3, 3, 9, 0]) == [0, 2, 3, 5, 9, 123]
    assert unique([-1]) == [-1]
    assert unique([]) == []
    assert unique([42]) == [42]
    assert unique([downcase('abc')]) == ['abc']
]
```
The function unique in this script accepts a list lst and returns a new list containing just the unique elements from that list, according to the problem statement. Additionally, the function goes the unique list's elements through the list and adds them to a set if they are not duplicates and not the special values [-None] or -illus. The function then uses the by creating a new list that contains only the elements that are not in the set and are not the special values. The test cases above demonstrate how the unique function works.