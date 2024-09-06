```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string"""
    return sorted(string, key=len, reverse=True)[:-len(string) // 2]

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

# Main program
if __name__ == "__main__":
    test_prefixes()
``` 
The code defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest character in the string. The `test_prefixes` function tests if the output of `all_prefixes` function is correct for a given input.  The main function serves as the entry point, and it executes the `test_prefixes` function to verify the correctness of the `all_prefixes` function.