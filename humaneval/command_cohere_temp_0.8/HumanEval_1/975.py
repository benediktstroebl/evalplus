Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separate parentheses groups.

The solution uses a stack to keep track of open parentheses and maintains a string builder to accumulate the content between the opened parentheses. Once an unmatched closing parenthesis is encountered or the stack is empty, the builder content is appended to the result list and reset. 

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result: List[str] = []
    stack: List[str] = []
    builder: str = ""

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                continue
            stack.pop()
            if not stack:
                result.append(builder)
                builder = ""
        else: 
            builder += char
            
    if builder:
        result.append(builder)
    return result
```

The provided example test case and output demonstrate the function's expected behavior:
```
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
``` 
The input string is first decomposed into its individual characters, and a stack is used to keep track of open parentheses. At the beginning of each iteration, the top item on the stack is checked; if it is not an open parenthesis, the character is added to the string builder. If it is an open parenthesis, it is added to the stack and discarded. Each closing parenthesis serves as a checkpoint; when it is encountered, the stack is checked for any open parentheses. If the stack is empty, the current builder is discarded. Otherwise, the top open parenthesis is popped from the stack, and the builder is kept for later. Once the loop is complete, any remaining content in the builder is added to the result list. The overall time complexity of this approach is O(n), where n is the length of the input string. The space complexity is O(n) as well due to the use of the stack and builder variables.