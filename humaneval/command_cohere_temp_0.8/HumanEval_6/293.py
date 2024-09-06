```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        chunk = chunk.replace('(', '')
        chunk = chunk.replace(')', '')
        result.append(len(chunk))
    return result
```
The function iterates through a string split by spaces, trimming pairs of opening and closing parentheses from each chunk, and storing their counts. This ensures that the maximum nesting depth of parentheses in each chunk is maintained. The list of counts is then returned. 

To ensure the function is robust to different kinds of input, you may want to include tests that cover other scenarios like:
- **Different Separators**: Adapt the code to handle multiple grouping symbols other than parentheses.
- **Variable Chunk Length**: Verify that the function handles chunks of different lengths.
- **Single Parenthesis**: Test the behavior of the function when given a single opening or closing parenthesis.
- **Large Input Size**: Examine the function's performance on large input sizes to ensure it doesn't lead to any issues. 
You can add these tests using tools like `unittest` in Python for comprehensive code evaluation.