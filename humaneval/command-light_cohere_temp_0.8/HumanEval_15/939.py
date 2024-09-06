```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """
   
    return ''.join(range(0, n+1)) + '\n'

# Test cases
test_string_sequence = StringSequenceTest(int)
test_string_sequence.test_string_sequence(0)
test_string_sequence.test_string_sequence(5)
print(test_string_sequence.test_string_sequence(20))
```