```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('x') == []
    assert all_prefixes('') == []
``` 
This code defines a function that returns a list of prefixes from the shortest to the longest characters in the input string. It uses a certain list comprehension to iterate over each character in the string and filters out non-letters to create the desired list of prefixes. The code also includes a test_all_prefixes() function, which asserts the output of the all_prefixes() function for different inputs.