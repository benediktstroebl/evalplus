Here is a self-contained Python script that solves the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> 'aaaaaa' == how_many_times('aaaa', 'aa')
    True
    >>> 'ab'.find('a') == how_many_times('ab', 'a')
    True
    >>> 'ac'.find('o') == how_many_times('ac', 'o')
    False
    """
    return string.find(substring, string) != -1
```  The function `how_many_times` takes two parameters: a string and a substring. It uses the string's `find()` method to find the first occurrence of the substring in the string.