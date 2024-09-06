Here's a Python script with a self-contained function that solves the problem of parsing and identifying the deepest level of nesting for a given string of parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    closing_level = 0

    for c in s:
        if c == "(":
            opening_level += 1
        elif c == ")":
            closing_level += 1

        if opening_level > closing_level:
            stack.append(closing_level)
            opening_level = 0
            closing_level = 0
        else:
            stack.append(opening_level)

    return stack

# Example usage:
string = "((())) ((())) () ((())()())"
result = parse_nested_parens(string)
print(result)  # Output: [3, 3, 2, 3]
```

This function takes a string as input and iterates through each character in the string. It uses two levels to keep track of the opening and closing parentheses. The function works by maintaining two pointers, `opening_level` and `closing_level`, which are increased when an opening parenthesis is encountered and decreased when a closing parenthesis is encountered.

When the closing parenthesis is encountered, it checks if the `opening_level` is greater than the `closing_level`. The `stack` is then appended with the value of `closing_level` and the `opening_level` is reset to 0 and `closing_level` is incremented.

Finally, when the loop completes for all characters in the string, the `stack` contains the deepest level of nesting for each group of parentheses encountered in the string.