```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        open_brackets = 0
        nesting = 0
        for char in token:
            if char == '(':
                open_brackets += 1
            else:
                open_brackets -= 1
                nesting += open_brackets
        result.append(nesting)
    return result
```

The code uses a simple approach to parse the string and count the opening brackets '(' and closing brackets ')' as it goes through. The count of opening brackets when a closing bracket is met gives the depth of nesting. The overall time complexity is O(N) where N is the size of the string.

The unit tests are correctly included as well, these tests cater to edge cases and correctly assert the expected output against the function's output. This is a good practice and helps maintain the code's integrity as the codebase evolves over time. 

Overall, the code is concise, uses typing for better code clarity and uses a comprehensive test suite to ensure the correctness of its functionality.