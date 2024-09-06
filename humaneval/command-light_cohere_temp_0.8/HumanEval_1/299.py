Here is a Python script with a self-contained function that solves the problem of separating out different groups of parentheses in a given string:
```python
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of well-formed parentheses from the input string.
    Each group should be balanced (each open brace is properly closed) and there should not be any spaces or nested parentheses.
    Input string should be in form of one or more balanced parenthesis groups
    """
    stack = []
    opening_braces = '([{){'
    closing_braces = ')}]'
    result = []
    for char in s:
        if char == opening_braces:
            stack.append(char)
        else:
            if len(stack) == 1 and stack[-1] == closing_braces:
                stack.pop()
                else:
                result.append(char)
   stack = []
    return result

# Test case
input_string = "( ) (( )) (( )( ))"
result_list = separate_paren_groups(input_string)
print("Separated Output: ", result_list)
```
This code defines a function `separate_paren_groups` that takes a string as input and returns a list of separated parenthesis groups. The code uses a balanced look to find and separate each balanced set of parentheses in the input string, without any spaces or nested parentheses.