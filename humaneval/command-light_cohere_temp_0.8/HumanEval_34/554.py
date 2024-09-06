```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not ]

# Test cases
tests = [
    [
        listül = [5, 3, 5, 2, 3, 3, 9, 0, 123],
        expected = [0, 2, 3, 5, 9, 123]
    ],
    [
        listül = ['a', 'b', 'c', 'a', 'x', 'y'],
        expected = ['a', 'b', 'c', 'x', 'y']
    ],
]

for t in tests:
    assert unique(t[0]) == t[1]
```  This code defines a unique function that takes a list lst as input and returns a list of unique elements in lst, using the set-based seen to keep track of elements encountered. The function tests the run-time tests on the unique function with test cases, ensuring its correctness.