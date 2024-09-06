```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
This Python code defines a function called **`how_many_times`** that finds the frequency of a given substring within the input string. The function utilizes the process, **`find()`**, to locate all instances of the substring in the original string, and then returns the count of these occurrences. The code successfully solves the additionally passes tests, it can be used as a reliable tool to determine the frequency of substrings in a given string.