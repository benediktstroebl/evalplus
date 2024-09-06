```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for seperated_string in s.split():
        string = ''.join(seperated_string.split())
        count = 0
        nested = 0
        i = 0
        while i < len(string):
            if string[i] == '(':
                count += 1
                nested = max(nested, count)
            elif string[i] == ')':
                count -= 1
            i += 1
        result.append(nested)
    return result
```
The algorithm employs a for loop to iterate through every space-separated sub-string of the input string s. For each substring, it counts the number of '(' and ')' characters to calculate the deepest level of nesting of parentheses. The maximum nesting level encountered in each substring is stored in the list result, which is then returned.  This solution passes the test case provided in the prompt and should correctly handle any string with valid parentheses.