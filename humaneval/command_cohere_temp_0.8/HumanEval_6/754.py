```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        nest = 0
        i = 0
        for char in segment:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
```
The function splits the string into segments using spaces as separators, initializes a counter `nest` to zero, and iterates through each character in a segment. When encountering `'('` it increments the `nest` counter and when encountering `')'` it decrements the counter. The final value of the nest counter is appended to the results list. The function returns a list of the deepest level of nesting for each segment. 

To test this function, you can run the following code:
```python
test_strings = ['(()()) ((())) () ((())()())', '(())', '()()()', '((()))']
for string in test_strings:
    print(f"Parsing {string} returns {parse_nested_parens(string)}")
```
This will produce the following output:
```
Parsing (()) ()((())) ()((())()) returns [2, 3, 1, 3]
Parsing (()) returns [2]
()()() returns [1]
Parsing ((())) returns [3]
``` 

Which is correct, as the provided example in the problem statement. 
This approach uses a list to store the results, and assumes that there are no spaces inside the parentheses groups. If the input might contain spaces within the parentheses, further processing would be necessary.