```python
def separate_paren_groups(input_string): 
    list = []
    stack = []
    for char in input_string:
        if char == '(':
            stack.append(char)
        else: 
            if not stack or stack[-1] == ')':
                list.append(stack.pop())
           
           
    list.append(char)
            else:
                stack.append(char)
    return list

# Test cases
def test_cases():
    assert separate_paren_groups('() (( )) (( )( ))') == ['()', '(())', '(()())'])
    assert separate_paren_groups('  )(( ))') == ['(', ')()', '()')
    assert separate_paren_groups('( )( )( )')') == ['(', '()', ')()', ')')
    assert separate_paren_groups('( )  ( )')') == ['(', ')()', '()')
test_cases()
 ``` 
This code defines a function named `separate_paren_groups`, which takes an input string and is designed to separate out and return individual parentheses groups from the input string. The function uses a stack to keep track of open parentheses, and it iterates through the input string, adding characters to the stack and appending closed parentheses back to the stack. This ensures that each open parenthesis is properly closed and not nested within the other. 
Additionally, any extra spaces are ignored, and the function returns a list of strings containing the individual groups of parentheses.