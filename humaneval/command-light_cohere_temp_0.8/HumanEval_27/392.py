```python
def flip_case(string: str) -> str:
    """
    Convert given string to have all characters flipped between lowercase and uppercase.
    Return string with all characters in lowercase transformed to uppercase and vice versa.
    """
Note: this method only works for text, not for symbols, numbers, etc. area codes, or other words in Markdown format.
# Example the input
#
string = "Hello"
# return "HELLO"

# Test case:
assert flip_case('Hello') == 'HELLO'

# Test case 2
assert flip_case('FOO') == 'foO'

# Test case 3
assert flip_case(' downstairs cat ' ) == 'towersdownscaT'
```