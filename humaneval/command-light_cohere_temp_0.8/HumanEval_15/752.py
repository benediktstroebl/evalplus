```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n.

    Returns: a sequence of numbers from 0 to n, inclusive. the end and concatenates them spaces between every number in the sequence."""
    
    #Positive Test Cases
    assert str(string_sequence(0)) == '0', 

    assert str(string_sequence(1)) == '1', 

    assert str(string_sequence(5)) == '0 1 2 3 4 5'

 
    #Negative Test Cases
    assert str(string_sequence(-1)) == '-1',

    assert str(string_sequence(-5)) == '-5-6'

    assert str(string_sequence(-10)) == '-10-11'

    assert str(string_sequence(-123)) == '-123-124'
```
The function `string_sequence` generates a string of numbers separated by spaces, starting from 0 and ending at the given number.