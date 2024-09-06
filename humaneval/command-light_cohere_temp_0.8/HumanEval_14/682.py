```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(). preferred(s) for s in string.
      .lambda x: x in (string for x in all_letters(x))]

def all_letters(char: str) -> List[str]:
    return [char] + all_letters(char[1:])

def all_preferred(string: str) -> List[str]:
    return [string[0]] + all_preferred(string[1:])

def all_letters_test(test_string):
    assert all_letters('bc') == ['b', 'c']
def all_preferred_test(test_string):
    assert all_preferred('hello') == ['o']
def all_prefixes_test(test_string):
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

# Run all the tests
all_letters_test('abc')
all_preferred_test('hello')
all_prefixes_test('abc')
 ```
This Python script defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of a given string. The `all_letters` function generates a list of all letters in a given string, and the `all_preferred` function generates a list of all preferred characters in a given string. The script also includes test cases to verify the correctness of the functions.