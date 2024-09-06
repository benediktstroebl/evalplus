```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """Separate groups of parentheses into individual strings.

    """
    
    return [ [char for char in input_string if char == ')' and ' ' not in input_string[:input_string.find('(') > 0)][char]
            if char == '(' and ' ' not in input_string[:input_string.find('(') > 0)][char]
                : input_string[input_string.find('(') > 0):[input_string.find('(') > 0) + 1:]
            : [char]

    # tests
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ) (( )) )()()' == ['()', '(())', '()()']
    assert separate_paren_groups(') ()() ()' == ['()', '()']
    assert separate_paren_groups('(()) ()()') == ['()', '(()')]
    assert separate_paren_groups(') ((() ))') == ['()', '()(']
    assert separate_paren_groups('() ( )() )()') == ['()', '()()']
    assert separate_paren_groups(' ( )() )') == ['()', '(']
    assert separate_paren_groups(' ( )() ) ()()') == ['()', '()()']
    assert separate_paren_groups('() ( ) ( )()') == ['()', '()()']
```