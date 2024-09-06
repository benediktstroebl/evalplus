```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, i, depth = 0, 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
            depth = max(depth, i + 1)
        else:
            forOpening -= 1
        i += 1
        if forOpening == 0:
            result.append(depth)
            depth = 0
    return result
```

The Python script provided defines a single function, `parse_nested_parens`, which takes a single argument, `s`, of type `str`. This function returns a list of `int` values.

This function iterates through the characters of the input string `s`. When it encounters an open parenthesis `(`, it increments a counter for the opening parenthesis, increases the index `i` of the current position in the string, and updates the `depth` to the maximum value of the current depth or the current index. When it encounters a closing parenthesis `)`, it decrements the counter for the opening parenthesis.

The function tracks the maximum depth of parentheses encountered in the string. When the counter for the opening parenthesis reaches zero, it means that a group of parentheses is closed. Consequently, the function updates the `result` list with the current depth, and resets the `depth` to 0 to continue parsing the next group of parentheses.

The list `result` finally returned by the function contains the maximum depth of nesting for each group of parentheses found in the string from the earliest occurrence to the latest one.