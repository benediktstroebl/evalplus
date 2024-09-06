```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all occurrences of a given substring within the original string, 
    including overlapping substring matches.
    Parameters: 
    string (str): input string 
    substring (sub): the substring to search for
    Returns: count of all occurrences of substring in string
    """
    return len([ i for i, match in enumerate(re.search(substring, string) ])

def test_how_many_times():
    assert how_many_times('aaaa', 'aa') == 3
```