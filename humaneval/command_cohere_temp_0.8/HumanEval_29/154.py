```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create a new list by applying a condition to each element of the existing list. 

To use the `filter_by_prefix` function, you can import it from the file it is contained in, which should be a valid Python module with a `.py` extension. For example, if the above code is in a file called `my_functions.py`, you can import it into a Jupyter Notebook like this:
```python
from my_functions import filter_by_prefix
```

If you'd like to test this function, you can write test cases in the same file as the function, like this:
```python
def test_filter_by_prefix():
    # Test case 1: Empty list, empty prefix
    assert filter_by_prefix([], ''), []

    # Test case 2: List contains matching strings, non-empty prefix
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test case 3: List contains non-matching strings, non-empty prefix
    assert filter_by_prefix(['123', '456', '789', 'abc'], 'a') == []
```

This block of code contains two asserts, each of which tests the function with a different input and checks whether the output matches the expected return value. When the code is run, if both assert conditions are true, the test passes. This is a basic example of unit testing, which can help to ensure that your functions are working as expected. 

This solution assumes that the input list contains strings, which is the most common assumption in the provided problem description, although this could be further clarified for more precise testing.