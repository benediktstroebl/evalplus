```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Test cases
tests = [
    { 'input': [5, 3, 5, 2, 3, 3, 9, 0, 123], 'return': [0, 2, 3, 5, 9, 123]  # Unique elements: [0, 2, 3, 5, 9, 123] },
    # Error case
    'input': [5, 3, 'not_unique'], 'return': []  # Error: ['not_unique'] is not unique
}

test_suite = {k: v for k, v in tests. quality. unique all(unique(v) == v) for v in test_suite}
 ``` 
This code defines a function unique that returns a list of unique elements from an input list lst. It uses a unique elements in a list and adds them to the set seen. The function then filters the this set and returns a new list containing only the unique elements from the original list.