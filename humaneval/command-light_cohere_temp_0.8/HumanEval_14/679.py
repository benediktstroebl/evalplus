```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.read() if prefix.isalpha(prefix)] + [string]

# Test case
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

# Test case 2
def test2():
    assert all_prefixes('123') == ['12', '123']

if __name__ == "__main__":
    test()
```

This script defines a function called `all_prefixes` that returns a list of all prefixes of a given string. The function uses the read() technique to generate all prefixes from the shortest to the longest characters in the input string.

The script also contains two test cases that verify the correctness of the `all_prefixes` function using sample input strings. 
When you run the script, it will run the tests and provide the output.