```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input and returns a new list containing only the strings from the input list that contain the given substring. 

The behaviour of the function is explained through tests in the code below:
```python
def test_filter_by_substring():
    # Testcase: Empty input list, empty output
    assert filter_by_substring([], 'a') == []

    # Testcase: Empty substring, full input preservation
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], '') == ['abc', 'bacd', 'cde', 'array']

    # Testcase: Substring found in some strings, proper output
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

    # Testcase: Ensuring case sensitivity
    assert filter_by_substring(['Abc', ' BACd', 'CdE', 'arrAy'], 'a') == ['Abc', ' BACd', 'arrAy']

test_filter_by_substring()
```

The test suite covers different scenarios, including empty input, empty substring, single-character substring, and case-sensitivity. 

To run the test suite, you can add the script above to a Python file (e.g., `filter_by_substring.py`) and execute the file. 

The following command will run the tests:
```bash
python filter_by_substring.py
```

The function and test cases provide a straightforward solution to filter a list of strings based on whether they contain a given substring.