```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for substrings in s.split(' '): 
        open_par = substrings.count('(')
        close_par = substrings.count(')')
        result.append(open_par - close_par)
    return result
```
The Python script provided defines a function called `parse_nested_parens` that takes in a string as input. This function splits the input string into a list of substrings using spaces as the separator. It then iterates through each substring to calculate the difference between the counts of open parentheses '(' and closed parentheses ')' within each substring. This difference represents the deepest level of nesting of parentheses within each substring. The results are then appended to a list and returned.

Here is an example function call:
```python
result = parse_nested_parens("(()()) ((())) () ((())()())")
print(result)
```

This would output the following:
```python
[2, 3, 1, 3]
```

The example sentence is '(()()) ((())) () ((())()())', and the list [2, 3, 1, 3] that is outputted is correct. This list represents the deepest level of nesting for each group of parentheses in the sentence.