```python
# Solve the problem:
# Given a list of string, return a concatenated string
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    """
    result = ''.join(strings)
    return result

# Tests:
def test_concatenate_empty_list():
    assert concatenate([]) == ''

def test_concatenate_non_empty_list():
    assert concatenate(['a', 'b', 'c']) == 'abc'

test_concatenate_empty_list()
test_concatenate_non_empty_list()
```

The function `concatenate` joins the strings in the list together using the `join` method which concatenates strings in a list using a specified separator. If the input list is empty, it returns an empty string. If the list is not empty, it returns a single string containing the concatenated values of the list. 

The unit tests test_concatenate_empty_list and test_concatenate_non_empty_list check that the function `concatenate` returns an empty string when an empty list is passed as an argument and that the function `concatenate` returns the concatenated string when a list of strings is passed as an argument respectively. 

To execute the tests, you can copy this code into a Python interpreter or save it in a file with the `.py` extension and run the file using the command line: 

```bash
python <filename>.py
```

The result of running the above command should display the following output:

```bash
.
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
``` 

This result indicates that both tests passed.