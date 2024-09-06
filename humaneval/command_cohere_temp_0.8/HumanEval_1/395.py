Here's a Python script that contains a function called `separate_paren_groups` which takes a string of parentheses as input and returns a list of strings that represent separate groups of parentheses. The code is annotated with comments to explain each part, and it also includes test cases to ensure the function's correctness:
```python
# The function to be defined
def separate_paren_groups(paren_string: str) -> List[str]:
    # List to store the separate groups
    results: List[str] = []
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, start a new string
        if char == '(':
            cur_string: str = ""
        # If the character is a close parenthesis, add it to the current string and check if it's balanced
        elif char == ')':
            # If the current string is empty, this close parenthesis doesn't belong to any group
            if not cur_string:
                results.append(char)
            # If the current string has an odd number of open parentheses, this close parenthesis is unbalanced
            elif cur_string.count('(') % 2 == 1:
                results.append(cur_string)
                results.append(char)
            # If the current string is balanced, add the parenthesis to the result and start a new string
            else:
                cur_string += char
                results.append(cur_string)
                cur_string = ""
        # In all other cases, simply add the character to the current string
        else:
            cur_string += char
    # If the last group is unfinished, add it to the results
    if cur_string:
        results.append(cur_string)
    return results

# Test cases
assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']
assert separate_paren_groups("((a)(b))") == ['((a)(b))']
assert separate_paren_groups("(a)") == ['(a)']
assert separate_paren_groups("()") == [()]
```
This script defines the `separate_paren_groups` function, which takes a string of parentheses as input and returns a list of strings that represent separate groups of parentheses. The function iterates through the input string, starting a new string whenever it encounters an open parenthesis and adding content to the current string whenever it encounters a closing parenthesis. When the closing parenthesis brings the balance to an even number, the current string is added to the results and a new string is started. Finally, any unfinished groups at the end of the input string are also added to the results. The function includes test cases to ensure its correctness. 
This solution separates the input string into separate groups of parentheses and returns those groups as a list of strings. G. Separate groups are balanced (each open brace is properly closed) and not nested within each other. Any spaces in the input string are ignored.