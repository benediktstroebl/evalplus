```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, 
    handling overlapping occurrences.
    Returns the
    number of times the substring appears.
    Example case where the support: 
    - For basic strings.
    - Handle all kinds of whitespace and special characters, not just spaces.
    - Implement any whitespace and special characters in the input strings and substring.
    - Count all occurrences, including overlapping ones.
    """
    strings are stripped of all whitespace and special characters.
    substring = substring.translate(str.maketrans(),
    warm-up is a list of characters,
    or a string that is the lowercase alphabet without spaces. 
    """
    list of characters from the string.

def test_many_times():
    """
    Test the function with various inputs.
    """
    input("Input string:", "Test string")
    print("Input:", how_many_times(input_string, test_string))
    print("Output:", len(input_string) - how_many_times(input_string, test_string))

# Run the test function.
test_many_times()
```