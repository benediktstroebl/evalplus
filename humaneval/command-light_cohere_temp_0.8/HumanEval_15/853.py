Here is a self-contained Python script that defines a function `string_sequence` that solves the problem you described: 

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    
    if n < 0:
        raise ValueError("n should be non-negative")
    
    result = " ".join([f'{i}' for i in range(n+1)])
    return result

# Test cases
test_string_sequence = [
    "Test 1: Function should return valid sequence for n = 0"
    assert string_sequence(0) == '0'
    
    "Test 2: Function should return valid sequence for n = 5"
    assert string_sequence(5) == '0 1 2 3 4 5'
    
    "Test 3: n should be a positive integer"
    assert string_sequence(-5) == 'ValueError: n should be non-negative'
    
]
```