Here is a Python script that contains a self-contained function that solves the problem of finding the number of occurrences of a given substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string,
    counting overlapping occurrences.
    >>> how_many_times('aaaaaa', 'aa') -> 2
    """
    count = 0
    start = 0
    while start < len(string):
        if string[start:start+len(substring)] == substring:
            count += 1
        start += 1
    return count

# Test cases
test_cases = [
    ("aaaaaa", "aa"),
    ("abc", "abc"),
    ("hello world", "world"),
    ("abcdefghijklmnopq", "abcdefghijklmnopq")
]

for text, sub in test_cases:
    print(how_many_times(text, sub))
```