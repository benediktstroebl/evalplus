```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses
    - Separate each balanced group into a separate string and return the list of those strings
    - For example, given "(abc)" -> "(), (def)" -> "(def())", and "((abc))", this function will return ['(", "), ("def")]
    """
    def separate(match):
        """ Return the part of the string matched by the given match object, with its matching group balanced."""
        # Find the last character of the match string, and subtract one to get the opening char.
        i = match.group(len.r[1,x
        -
        # If the matched string is longer than the opening char, use slice to remove it
        # and add one to get the closing char.
        return i + (match[i:match.group().len()-1)+ 1)
    else:
        return match[match.group(1).0:match.len()-1un-os the Shaker style that will break the matched string into separate parts.
    return '(' + separate(match[i+1:match.group(1).0]) + ')'
def test_function() -> None:
    """ Test the separate_paren_groups function by passing some test strings and checking the results."""
    test_strings = [
        "()(( ))(( ))",
        "( )(()())",
        "( )  ((  ))",
        "((  )())",
        "(( )))"
    ]
    expected = [',(', '(()())', '()', '()()', '()')
    for string, expected_list in zip(test_strings, expected):
        actual = separate_paren_groups(string)
        assert actual == expected_list, f"Error in test string: {string}, expected: {expected_list}"
    ```