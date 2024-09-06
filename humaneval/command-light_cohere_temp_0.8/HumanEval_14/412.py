```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' + char for char in string]

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'ac', 'bc', 'bd']
    assert all_prefixes('xyzt') == ['xy', 'yx', xz]
test_prefixes()  # Main function to run tests
``` 
The code defines a function called **`all_prefixes`** that returns a list of all prefixes from the shortest to the longest of the input string. It uses list comprehension and simply iterates the characters in the input string and adds each one prefixed with 'a' to create a new prefix. 
The test cases validate the expected output of the function for different input strings.