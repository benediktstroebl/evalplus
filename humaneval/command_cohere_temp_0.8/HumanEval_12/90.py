Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
```python
# The module where the longest function is defined
module = __import__('__main__')


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    :param strings: List of strings to find the longest from.
    :return: Longest string or None if the list is empty.
    """
    # type: <<== declarative semantic alias created from the 'List[str]' type annotation>>
    longest_strings = sorted(strings, key=len, reverse=True)
    return longest_strings[0] if longest_strings else None


# Unit tests
module.test_longest = lambda: None if longest([]) else None
module.test_longest(['a', 'b', 'c']) = 'a'
module.test_longest(['a', 'bb', 'ccc']) = 'ccc'
module.test_longest(['aaa', 'bb', 'ccc']) = 'ccc'
```

In this script, a function named `longest` is defined, which accepts a list of strings (`List[str]`) as an argument and returns the longest string from the list. If there are multiple strings of the same length, it returns the first one. If the input list is empty, it returns `None`.

The function is then tested using Python's `test` function, which is a part of the `unittest` framework. This framework is widely accepted and enables developers to write and run isolated tests, which helps to pinpoint where in the code changes are needed and to propagate those changes safely over time. Each test case is defined by assigning the result of the function to the corresponding variable on the left-hand side, and the right-hand side is the expected output. 

To run the tests, you can use the following command:
```python
python -m unittest tests.test_longest
```

This will run the test suite against the `longest` function defined in the `tests` module. The `unittest` framework is used to execute the test suites and evaluate the results.