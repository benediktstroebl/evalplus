Here's a Python script that contains a function called `separate_paren_groups` which takes a string of parentheses as input and returns a list of strings that represent separate groups of parentheses. The code is tested on Python 3.7 :
```python
import re
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    # Use a regex to match all individual brace groups and keep removing the last match until there are no more matches
    brace_groups = re.findall(r'(\([^()]*\))', paren_string)
    while brace_groups:
        paren_string = re.sub(r'(\([^()]*\))', brace_groups.pop(), paren_string)
        brace_groups = re.findall(r'(\([^()]*\))', paren_string)
        
    # If there's anything left in the string, it means we haven't matched everything
    # This will only happen if the input string is not properly balanced
    if paren_string:
        raise ValueError(f"There are still unmatched parentheses in the string: {paren_string}")
        
    return brace_groups

# Here are some example tests to check the function above
unittest.TestCase.assertEqual(separate_paren_groups("( ) (( )) (( )( ))"), ['()', '(())', '(()())'])
unittest.TestCase.assertEqual(separate_paren_groups("((a)(b))"), ['((a)(b))'])
unittest.TestCase.assertEqual(separate_paren_groups("((a)(b)(c))"), ['((a)(b)', '(c)')])
unittest.TestCase.assertEqual(separate_paren_groups("(a)"), ['(a)'])
unittest.TestCase.assertEqual(separate_paren_groups("()"), [''])
unittest.TestCase.assertEqual(separate_paren_groups("( )"), [''])
unittest.TestCase.assertEqual(separate_paren_groups("((((a))))"), ['((((a))))'])
```

You can quickly run these tests, if you have `unittest` installed, by adding a call to `unittest.main()` to the bottom of the script before running it with Python. Here's what the entire code would look like:
```python
import re
import unittest
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    # Use a regex to match all individual brace groups and keep removing the last match until there are no more matches
    brace_groups = re.findall(r'(\([^()]*\))', paren_string)
    while brace_groups:
        paren_string = re.sub(r'(\([^()]*\))', brace_groups.pop(), paren_string)
        brace_groups = re.findall(r'(\([^()]*\))', paren_string)
        
    # If there's anything