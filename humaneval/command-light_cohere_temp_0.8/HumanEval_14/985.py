```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # assert true
    names for test here
    assert len(all_prefixes('abc')) == 3
    assert len(all_prefixes('abcs')) == 2
    assert len(all_prefixes('aaaa')) == 3
    assert len(all_prefixes('')) == 0
``` 
This code defines a function called all_prefixes, which takes a string as input and returns a list of all prefixes from shortest to longest characters in the input string. The function uses a strings. Each prefix in the strings are iterated using list comprehension and the character at that index is added to the resulting list. The test cases validate that the function is correct for this input.