```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case 1: Basic string filtering
test_case_1 = [ 'abc', 'bcd', 'cde', 'array' ]
test_case_1_expected = ['abc', 'array']

# Test case 2: List of strings containing different prefixes
test_case_2 = ['john', 'bob', 'doe', 'jane']
test_case_2_expected = ['john', 'bob', 'doe']

# Test case 3: Nested strings
test_case_3 = ['folder', 'folder/subfolder', 'jpg', 'txt']
test_case_3_expected = ['folder/subfolder', 'jpg']

# Run the function and compare the results with expected outputs
print(filter_by_prefix(test_case_1, 'a'))
print(test_case_1_expected)
print(filter_by_prefix(test_case_2, 'j'))
print(test_case_2_expected)
print(filter_by_prefix(test_case_3, '.'))
print(test_case_3_expected)
``` 
This Python script provides a function called `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a filter the list of strings that start with the specified prefix. It uses the basic list comprehension to achieve this. 

Test cases are also provided, each one containing a list of strings and an expected output. The script then runs the function with each test case and compares the output with the expected output to validate the functionality of the function.