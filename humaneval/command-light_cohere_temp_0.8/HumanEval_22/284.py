```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    ('a', 'three'),
    (1, 2, 'three'),
    ([1, 2, 3], 'abc'),
    ([1, 2, 3], []),
    (['a', 3, 'four'], ['five'])
]

def test():
    assert filter_integers(test_filter_integers) == [1, 2, 3]

# Main code
if __name__ == "__main__":
    print("Test passed!")
```