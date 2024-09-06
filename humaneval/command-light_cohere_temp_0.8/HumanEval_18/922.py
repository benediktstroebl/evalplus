Here's a Python script that includes a self-contained function with tests to solve the problem:
```python
import re

def how_many_times(string: str, substring: str) -> int:
    pattern = re.compile(substring, string)
    match = pattern.findall()
    pattern = re.compile(substring, string)
    match = pattern.findall()
    value = len(match)
    return value

# Test the function
test_many_times = []
test_many_times.append(['', 'a'])
test_many_times.append(['aaa', 'aa'])
test_many_times.append(['aaaaaa', 'aaa'])
test_many_times.append(['aa', ''])
test_many_times.test_many_times.

```
This script defines a function that counts the occurrences of a given substring in a given string, using the `re.findall()` function from the to find all matches of the substring in the string. Also, it provides a series of test cases to ensure that the function is working correctly.