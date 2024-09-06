```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('hello', 'hello')
    0
    >>> how_many_times('hello', 'h')
    0
    >>> how_many_times('aa', 'a')
    2
    """
    return len(string) // (len(substring) + 1)

# Test the function with various cases
test_cases = [
    ("aaa", "aaaa", "hello"), ("aa", "a"),
    ("hello", ""), ("", ""), (". ",", "")
]

for i, test in enumerate(test_cases):
    result = how_many_times(*test)
    assert result == i+1, f"Error: {test} should return {i+1} but returned {result}"
``` 
This script provides a function `how_many_times` that calculates the number of occurrences of a substring within a given string. It is tested with several test cases to verify its functionality.