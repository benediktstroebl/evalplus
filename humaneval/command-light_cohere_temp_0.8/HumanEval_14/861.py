```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])

def all_prefixes_test(test_string: str) -> None:
    actual_result = all_prefixes(test_string)
    expected_result = ['a', 'ab', test_string[0]] + all_prefixes(test_string[1:])
    assert actual_result == expected_result, f"Check failed: {actual_result}, {expected_result}"

# Test the function with an example
all_prefixes_test('abc')
 ```
This Python code demonstrates a function called **`all_prefixes`** that returns a list of all prefixes from shortest to longest of an input string. This function uses the strings are passed to the function, and the function returns a list of all prefixes in ascending order. The test function is then used to test the correctness of the all_prefixes function with a sample input.