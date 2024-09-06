Here's a Python script with a self-contained function that solves the problem using a recursive approach, along with corresponding test cases:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    def parser(i, opened, acc):
        if i == len(s):
            return acc
        if s[i] == '(':
            opened[0] += 1
            acc.append(parser(i+1, opened, acc))
        elif s[i] == ')':
            opened[0] -= 1
            if opened[0] < 0:
                return acc
            acc.append(parser(i+1, opened, acc))
        elif ' ' in s[i:] and opened[0] == 0:
            j = i+1
            while s[j:j+1] != ' ':
                j += 1
            acc.append(parser(j, opened, acc))
        return acc
    
    if ' ' not in s:
        return [0]
    opened = [0]
    return parser(0, opened, [])

# Test cases
assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
assert parse_nested_parens("(((((()())))))))")) == [5]
assert parse_nested_parens("(a)(b)())" "((()))") == [2, 2, 1, 1]
```

This script uses a recursive approach to parse the input string s, keeping track of the current opening parentheses count as it iterates through the string. The function `parser` runs until it reaches the end of the string or encounters a closing parenthesis, and it concatenates the results of recursive calls to provide a list of deepest nesting levels for each group of parentheses.