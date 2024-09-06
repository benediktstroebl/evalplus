```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not (-1)]

# Test cases
tests = [
    {
        'input': [5, 3, 5, 2, 3, 3, 9, 0, 123],
        'expected': [0, 2, 3, 5, 9, 123]
    },
    {
        'input': '-1, 5, 3, 5, 2, 3, 3, 9, 0, 123',
        'expected': [-1]
    },
    {
        'input': [1, 2, 3, 4, 3, 5],
        'expected': [1, 2, 3, 4, 3, 5]
    },
]

for test in tests:
    assert unique(test['input']) == test['expected'],
    print('Passed:', test['input'], '->', test['expected'])
``` 
This code defines a function unique which takes a list lst as input and returns a new list containing only the unique elements from the original list. It utilizes a unique() function which takes a set as input and creates a new set from the elements in the input set, which are the unique elements in the list. The set is then converted back to a list using list(set) and the unique elements from the original list are returned. The test cases section includes a set of test cases that pass the unique function to ensure its correctness.