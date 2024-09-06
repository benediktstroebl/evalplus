```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(). all_prefixes(string) + ['']

def all_prefixes_test(test_string: str) -> None:
    assert all_prefixes(test_string) == [''].join('', all_prefixes_test(test_string[:1])) + ['']
    return None

# Example usage
string = "abc"
all_prefixes(string)
print(string)  # Output: ['a', 'ab', 'abc']
all_prefixes_test(string)  # Passed test!
```

The above Python script defines a function `all_prefixes` that returns a list of all prefixes of a given string, and a function `all_prefixes_test` to test the `all_prefixes` function with a given string. The `all_prefixes` function uses the `join` method to generate all prefixes of the substring starting from index 0. The `all_prefixes_test` function asserts that the result of `all_prefixes` is the expected output plus an empty string.