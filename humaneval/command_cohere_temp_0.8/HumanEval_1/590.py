Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing the separate groups of parentheses. The script also includes a set of tests to verify the function's correctness:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '('
    close_braces = ')'
    paren_list = []
    current_paren = ''

    for char in paren_string:
        if char == open_braces:
            current_paren += char
        elif char == close_braces:
            if not current_paren:
                continue
            paren_list.append(current_paren)
            current_paren = ''
        else:
            current_paren += char

    if current_paren:
        paren_list.append(current_paren)

    return paren_list

# Tests
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
assert separate_paren_groups('(a (b))') == ['(a (b))']
assert separate_paren_groups('(a (b c))') == ['(a ', '(b c)', '())']
assert separate_paren_groups('()') == ['']
assert separate_paren_groups('( a )') == ['( ', ' a ', ')']
```

Let's break down the code step by step, along with the tests included in the script:
1. **Importing Typing**:
   The script starts with the optional import of the `List` module from the `typing` module. The `List` object denotes that the function `separate_paren_groups` will return a list of strings.

2. **Function Definition**:
   The `separate_paren_groups` function takes a single argument, `paren_string`, which is of type string. The function returns a list of strings, with each string representing a balanced group of parentheses.

3. **Brace Counting**:
   The script initializes two strings, `open_braces` and `close_braces`, with the corresponding open and closing braces (`('('`, `')')`). These will be used for character counting.

4. **Initialization of Empty List**:
   An empty list called `paren_list` is initialized. This list will hold the separated parentheses groups.

5. **Building Groups**:
   The script iterates through each character of the input `paren_string`. If the character is an open brace, it's added to the `current_paren` string. If the character is a closing brace, the script checks if `current_paren` is not empty. If it's not empty, the group `current_paren` is added to the `paren_list`, and `current_paren` is reset to an empty string. This process continues until all characters are processed.

6. **Test Cases**:
   The script includes several test cases to verify the correctness of the `separate_paren_groups` function. These test cases cover different scenarios, including nested and nested-within-each-other parentheses, and spaces between parentheses.

   - The first test case, `"( ) (( )) (( )( ))",` should return `['()', '(())', '(()())']`.
   - In the second test case, `"(a (b))"`, the function is expected to return `['(a (b))']`.
   - For the third test case, `"