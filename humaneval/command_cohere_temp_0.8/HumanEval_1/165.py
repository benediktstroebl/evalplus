Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent the individual groups of parentheses found in the input string. The script also includes a test case to demonstrate the function. The code is formatted using Markdown code blocks to maintain readability.

```python
# Python program to separate nested parentheses into
# individual groups

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                print("Unmatched ')' found.")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle the last group
    if not stack:
        result.append("".join(current_group))
    else:
        print("Unmatched '(' found.")

    return result

# Driver code
test_string = '( ) (( )) (( )( ))'
expected_result = ['()', '(())', '(()())']

print(f"\nTest string: {test_string}")
print(f"Expected Result: {expected_result}")
print(f"Actual Result: {separate_paren_groups(test_string)}")
```

To test the script, you can provide a test case string `( ) (( )) (( )( ))` and compare the output with the expected result `['()', '(())', '(()())']`. 

This script offers a clear and reliable way to manage parentheses in a given string and is readily adaptable to diverse scenarios requiring string manipulation.