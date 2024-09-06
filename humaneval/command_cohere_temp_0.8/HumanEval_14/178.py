```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the strings and omit elements whose first member is the NULL string (indicative of an empty string).  The iterated result is then reversed to list the prefixes in order from longest to shortest. 

The logic behind the function is to iterate over the strings and chop off a part of the string from the beginning, starting from the first character until it reaches an empty string (when the prefix is equal to the full string). The dropped prefixes are stored in a list, and then the list is reversed to order the prefixes from longest to shortest. 

The unit tests would look like this:
```python
def test_all_prefixes():
    assert all_prefixes("abc") == ["a", "ab", "abc"]
    assert all_prefixes("axbxcxd") == ["", "a", "ax", "axb", "axbxc", "axbxcxd"]
    assert all_prefixes("abcde") == ["", "a", "ab", "abc", "abcd", "abcde"]
```
You can then run the tests by typing `python test_all_prefixes.py` in any Python environment.  This will run the tests, and upon completion, you will see an output similar to `OK` if the tests pass and the code works as expected.  If there's a mistake, an elaborative error message will be displayed alongside the exact point of contract failure.  This will help you pinpoint and rectify the problem.  Thus, it allows you to validate your code and confirm it operates according to the problem statement.  This will additionally help uphold code correctness and robustness.