Here's the self-contained Python script that defines a function `string_sequence` solving the problem you described: 

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return " ".join([f'{i}' for i in range(n)])

# Test cases 

def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'

if __name__ == "__main__":
    test_string_sequence()
```

The test case function `test_string_sequence` does `assert` calls to check if the `string_sequence` function is working correctly with different input values.  The test_string_sequence() is called to run the test cases.