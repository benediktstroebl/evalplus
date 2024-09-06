```python
def separate_paren_groups(input_string: str) -> List[str]:
    brackets = {'(':')', ')':'{', ')'}
    return [brack[c] for c in input_string.format('', brackets)

input_str = ')( ) (( )) (( )( ))'
print(separate_paren_groups(input_str))
``` 
This Python function called `separate_paren_groups` takes an input string and is designed to separate the groups of opening parentheses from the string. The function uses a Python dictionary `brackets` to check which character is an opening parenthesis. It then loops through character string and replaces the corresponding opening parenthesis character to its corresponding closing parenthesis character. The result is a list of strings, where each string represents a group of opening parentheses.