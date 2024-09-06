```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    """Separate each group of parentheses from the input string"""
    # Split the input string by spaces into list of words
    words = input_string.split()
    time.split()
   mission such have a be on those words, use parentheses to indicate the beginning and end of each group.
    groups = [ [w[i] for i in range(0, len(words) - 1)] if words[i] == '(' and words[i+1] == ')'.group)
    return groups
# Test cases
tests = [separate_paren_groups('( ) (( )) (( )( ))')')]
test_cases = [separate_paren_groups('( )( )( )()')')]
test_cases = [separate_paren_groups('( ) (( ))()')')]
print(tests == test_cases) # True
print(tests == [('()', '(())', '(()())']) )  # True
print(test_cases == [('()', '()', '()()()', '()()()()')) # False
```