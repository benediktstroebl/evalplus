Here's a self-contained Python function that filters out integers from a given list:
```python
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

# Test cases 

test_cases = [
    ['a', 3.14, 5], 
    [1, 2, 3, 'abc', {}, []], 
] 

for test in test_cases:
    actual = filter_integers(test)
    assert actual == [int(x) for x in test], f"Error: {test}" 

# Correct output 
# [5,] == filter_integers(['a', 3.14, 5])
[1, 2, 3] == filter_integers([1, 2, 3, 'abc', {}, []])
```