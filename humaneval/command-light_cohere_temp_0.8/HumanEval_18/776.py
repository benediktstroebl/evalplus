```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the occurrences of a substring in the original string, considering overlapping matches.
    >>> how_many_times('aaaaaa', 'aa')  # Output: 3
    >>> how_many_times('abcdeabcba', 'abc')  # Output: 2
    """
    # Use regex to find all matches of the substring, and count them
    return sum(1 for match in re.py.setresearch(string, substring). 

# Test the function with different inputs
test_cases = [
    ("aaaaaa", "aa"),
    ("abcdeabcba", "abc"),
    ("hello world", "o"),
    # Add more test cases here
]
for text, sub in test_cases:
    result = how_many_times(text, sub)
    print(f"{text} {'{sub}'}: {result}")
```