```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases are defined here with the help of the unittest module
import unittest

class TestFilterBySubstring(unittest.TestCase.TestCase.TestCase):
    test function:
    def test_filter_by_substring():
        # Test case 1
        strings = ['abc', 'bacd', 'cde', 'array', 'hello']
        sub = 'a'
        expected = ['abc', 'bacd', 'array']

        # Test case 2
        strings = ['def', 'abc', 'cba']
        sub = 'a'
        expected = []

        # Test case 3
        strings = ['a', 'b', 'cd']
        sub = 'c'
        expected = []

        # Test case 4
        strings = ['a', 'b', 'cd', 'abc']
        sub = 'ab'
        expected = ['abc']

        # Test case 5
        strings = ['a', 'b', 'cd', 'abc']
        sub = ''

        # Test case 6
        strings = ['abc', 'b', 'cd']
        sub = 'a'

        # Test case 7
        strings = ['abc', 'def']
        sub = 'e'

        # Test case 8
        strings = ['abc', 'abcd', 'def']
        sub = 'a'

        # Test case 9
        strings = ['abc', 'abc']
        sub = 'c'

        # Test case 10
        strings = ['a', 'b']
        sub = 'bc'

        # Testing individual cases
        test_case_1(strings=strings, sub=sub, expected=expected)
        test_case_2(strings=strings, sub=sub, expected=expected)
        test_case_3(strings=strings, sub=sub, expected=expected)
        test_case_4(strings=strings, sub=sub, expected=expected)
        test_case_5(strings=strings, sub=sub, expected=expected)
        test_case_6(strings=strings, sub=sub, expected=expected)
        test_case_7(strings=strings, sub=sub, expected=expected)
        test_case_8(strings=strings, sub=sub, expected=expected)
        test_case_9(strings=strings, sub=sub, expected=expected)
        test_case_10(strings=strings, sub=sub, expected=expected)

    if __name__ == '__main__':
        unittest.main()

```
The above Python script defines a function called `filter_by_substring`, which takes a list of strings and a substring as input and returns a new list of strings containing only the elements of the original list that contain the given substring. 

The script also includes 10 test cases for the `filter_by_substring` function, using the `unittest` module to define and run the tests. 
The test cases cover different scenarios, including empty strings, different lengths of strings and substrings, and different combinations of strings and substrings. 
Finally, the `unittest.main()` function is execute the script, which runs all the test cases and checks if the `filter_by_substring` function is working correctly.