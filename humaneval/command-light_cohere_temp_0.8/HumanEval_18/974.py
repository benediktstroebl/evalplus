```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    handling overlapping substring matches.

    Parameters: 
    string: str, the original string 
    substring: str, the substring to search for 

    Returns:
    int, the number of times the substring appears in the string
    """
    return sum(1 for i, x in enumerate(string.find(substring), string.find(substring): 
        , re.match=True))

# Test cases
test_cases = [
    ("", "a"),  # returns 0
    ("aaaa", "aa"),  # returns 3
    ("hello world", "o"),  # returns 2
    ("abcde", "abc"),  # returns 3
]

for text, expect in test_cases:
    got = how_many_times(text, text)
    print(f"{text} -> {got}")
    print(f"Expected -> {expect}")
    assert got == expect
```