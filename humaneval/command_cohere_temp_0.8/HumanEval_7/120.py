```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings `strings` and a substring `substring`. It returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, where each string in the input list is checked to see if the substring is a part of it. If it is, the string is added to the result list. 

To follow the expected behavior of the function, an example of its usage is provided:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ar')
['array']
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'xyz')
[]
```

This example test suite contains three test cases that cover different scenarios. Firstly, when the substring 'a' is provided, the function is expected to return the complete list of strings that contain this character, which is achieved by the list comprehension `[s for s in strings if substring in s]`. For the second test case, where the distinctive substring is 'ar', the expected behavior is for the function to return only one string that contains these characters, 'array'. Lastly, the test case for `xyz` is goaled to test whether the function correctly handles the scenario when the substring is not present in any of the strings of the list, thus returning an empty list. 

The function is designed to be efficient and straightforward, allowing for easy testing and debugging. It can be easily optimized further if needed, but this basic implementation is a good starting point and will work correctly to filter strings containing a specified substring.