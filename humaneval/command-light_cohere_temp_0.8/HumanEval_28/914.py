```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string """
    return ''.join(strings) 

def test_concatenate(): 
    strings = ['a', 'b', 'c']
    result = concatenate(strings)
    assert result == 'abc', "Function does not return expected value" 
    return result

# Run the test
print(test_concatenate())
```
The code defines a `concatenate` function that takes a list of strings as an argument and returns the concatenated string. The `test_concatenate` function contains a test case with a sample string and asserts the result against the expected output. 
When you run this code, it will print the test case and the result should pass the assertion.