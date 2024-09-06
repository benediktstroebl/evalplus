```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
test_get_positive = [
    {'input': [-1, 2, -4, 5, 6],
     'expected': [2, 5, 6]
     },
    {'input': [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
     'expected': [5, 3, 2, 3, 9, 123, 1]
     },
    {'input': 'abc123', 'expected': []
     },
]

for test_case in test_get_positive:
    assert get_positive(test_case['input']) == test_case['expected'])
```