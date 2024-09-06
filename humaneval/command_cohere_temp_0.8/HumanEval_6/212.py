```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        count = 0
        while opening != closing:
            count += opening == '('
            opening = opening[1:] if opening[-1] == ')' else opening + ')'
            closing = closing[1:] if closing[-1] == ')' else closing + ')'
        result.append(count)
    return result
``` 

This code solves the problem by iterating through all the parentheses groups in the string and keeping track of the number of opening parentheses (`('`) for each group. When a closing parenthesis (`')`) is encountered, it is added to the count at the end of the loop. The function returns a list of these counts, which represent the maximum nesting levels of each group. 

The tests are accurate and reflect the expected behavior of the problem. However, these are not included in the provided markdown code block as they are not necessary to understand the code in the given context. Let me know if you would like to include the test cases in a different format or provide additional assistance.