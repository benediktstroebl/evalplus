```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, returns the longest one.
    Args: 
    strings (List[str]): List of strings 
    Returns: 
    List[str]: The longest string from the input list
    """
    return max(strings, key=len) if strings else None 
# Unit tests
def test_longest():
    long_list = ['a', 'bb', 'ccc']
    longest_result = longest(long_list)
    assert longest_result == 'ccc' 

# Example usage
test_longest() 
``` 
This script defines the `longest` function, which takes a list of strings as input and returns the longest string. The function uses the max function with the `len` key to find the maximum length and returns the corresponding string. The test case ensures that the code behaves as expected and passes all tests.