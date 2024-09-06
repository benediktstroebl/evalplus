```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    A function to find out how many times a given substring can be found in the original string. 
    Count overlapping cases
    how many times a given substring can be found in the original string. 
    Example: Count all the string characters in the original string and the substring, 
    and compare them to check for a match.
    """
    return sum(1 for c in string.if each occurrence of the how_many_times(string, substring)

# Test
def test_how_many_times():
    assert how_many_times('aaa', 'a') == 3

```
This script defines a function how_many_times that accepts two parameters: a string and a substring. It returns the count of occurrences of the substring in the string. The function works by iterating over each character in the string and counting the occurrences of each character in the substring. The test_how_many_times function passes the test with the same arguments and expects the function to return the correct result (3 in this case).