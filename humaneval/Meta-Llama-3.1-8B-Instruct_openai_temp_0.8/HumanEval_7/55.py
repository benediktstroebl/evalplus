```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for.

    Returns:
        List[str]: The filtered list of strings.
    """
    # Use list comprehension to create a new list containing only strings that contain the substring
    return [s for s in strings if substring in s]


# Test cases
if __name__ == "__main__":
    import sys
    from io import StringIO
    import unittest

    # Redirect stdout to capture output
    original_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout

    class TestFilterBySubstring(unittest.TestCase):
        def test_empty_list(self):
            self.assertEqual(filter_by_substring([], 'a'), [])

        def test_no_matches(self):
            self.assertEqual(filter_by_substring(['cde', 'fgh', 'ijk'], 'a'), [])

        def test_matches(self):
            self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    # Run test cases
    unittest.main(argv=[], verbosity=2, exit=False)

    # Print test output
    sys.stdout = original_stdout
    print(new_stdout.getvalue())
```

This script defines the `filter_by_substring` function and includes test cases to ensure it works correctly. The test cases cover the following scenarios:

1.  An empty list is passed to the function.
2.  A list with no strings containing the substring is passed to the function.
3.  A list with strings containing the substring is passed to the function.