```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, '']]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [None, ''],
    ['a', 'b', 'c', 'a'],
    [123, '456']
]

for test_case in test_cases:
    actual = unique(test_case)
    assert actual == [x for x in test_case if x != '' and x not None]
```  This code defines a function unique that returns a list of unique elements from a given list lst, based on the set-like implementation. 

It then provides test cases, which are passed to the unique function and compared to the resulting list of unique elements using assertions.