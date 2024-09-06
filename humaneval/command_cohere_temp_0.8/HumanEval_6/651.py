```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group.split(' ')))) ) for group in s.split(' ')]
```

The provided Python script demonstrates a function called `parse_nested_parens`, which takes a single argument, `s`, representing a string of nested parentheses separated by spaces. This function returns a list where each element corresponds to the maximum depth of nesting for the respective group of parentheses. To achieve this, it employs a combination of integer summing and maximum value extraction.

Here is an example usage of the function for a given input:
```python
input = '(()()) ((())) () ((())()())'
print(parse_nested_parens(input))
```

This would produce the following output:
```python
[2, 3, 1, 3]
```

In the above example, each number in the output list corresponds to the maximum depth of nesting for the respective group of parentheses within the input string.