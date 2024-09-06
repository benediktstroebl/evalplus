```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


# Test suite
test_suite = []
strings = ["abc", "bacd", "cde", "array", "xyz"]
substrings = ["a", "x"]

test_suite.add(filter_by_substring(strings, substrings))

# Print test results
for test in test_suite:
    print(test)
 ``` 
This Python code defines a function `filter_by_substring` that filters a list of strings based on containing a given substring. The function takes two input arguments: a list of strings `strings` and a substring `substring`. 

It uses list comprehension to create a new list containing only the elements from the original strings list that contain the given substring. 

The code then defines a simple test suite with a list of strings and a list of substrings, and adds the result of the `filter_by_substring` function to the test suite. 

Finally, the code prints the test results, showing which strings from the input list contain the given substring.