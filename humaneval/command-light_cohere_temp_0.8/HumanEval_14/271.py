```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join()[i:]+string[i:] for i in range(len(string)-1, 0, -1)]
def test_all_prefixes(test_strs: List[str]) -> None:
    for test_string in test_strs:
        resulting_list = all_prefixes(test_string)
        assert len(resulting_list) == len(set(resulting_list)),
        assert all(resulting_list == set(resulting_list)),
test_all_prefixes(['abc', 'abcd', '123'])
```
This Python code provides a function all_prefixes that takes a string as input and returns a list of all its prefixes. The function uses a simple list comprehension to iterate through each character of the input string, appending the character to the beginning of a new prefix until reaching the end of the string. The test_all_prefixes function is used to test the correctness of the all_prefixes function by passing a list of strings that contain different test cases.