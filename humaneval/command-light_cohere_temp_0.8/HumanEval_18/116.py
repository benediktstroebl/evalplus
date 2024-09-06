Here is a Python script that contains a self-contained function that solves the problem of finding the number of times a given substring can be found in the original string, while accounting for overlapping substring occurrences:
```python
def how_many_times(string: str, substring: str) -> int:
    return len(string) - len(set(string.find(substring)))</ellate_me()

def find(substring):
    return [i for i, char in enumerate(substring) if char in string]

def length(string):
    return len(string)

def isubstring_in(string, substring):
    return substring in string

def __tests__():
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abcde", "ab") == 2
    assert how_many_times("aaaa", "a") == 3
    assert how_many_times("aaa", "aa") == 0
    assert how_many_times("aaa", "b") == -1
    assert how_many_times("ABCDE", "abcde") == 2
    assert isubstring_in("abcde", "ab") == True
    assert isubstring_in("", "abcde") == False
```
This script defines a function `how_many_times` that calculates the number of occurrences of a given substring in a given string. It also has helper functions for string manipulation, including `find` for character existence and `length` to determine the length of a string.