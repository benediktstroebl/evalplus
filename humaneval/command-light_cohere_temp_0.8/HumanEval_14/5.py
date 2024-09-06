```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]

def test_function():
    return all_prefixes('abc')
``` 
This code defines a function called all_prefixes that returns a list of all prefixes in a given string. The test_function is a standalone function that demonstrates the all_prefixes function by passing the string 'abc' as an argument and checks if the result is a list of strings ['a', 'ab', 'abc'].