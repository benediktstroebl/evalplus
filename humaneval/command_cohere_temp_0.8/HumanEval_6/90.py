```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair in s.split():
        count = 0
        nesting_level = 0
        for char in bracket_pair:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            nesting_level = max(nesting_level, count)
        result.append(nesting_level)
    return result
```

The specified Python script solves the problem using a single function named `parse_nested_parens`. This function takes a string as input, and returns a list of deepest nesting levels of parentheses in each group.

To achieve this, the function follows these steps:
1. It splits the input string into a list of **string chunks** using space as a separator. Each chunk represents a group of parentheses.
2. For each chunk, it initializes `nesting_level` and `count` to keep track of the deepest level of nesting and the number of opening parentheses encountered.
3. The function iterates through each character in the chunk. If the character is `'('` (opening parentheses), it increments the `count`. If it's `')'` (closing parentheses), it decrements the `count`. The `nesting_level` is updated with the maximum value of `count` encountered, which represents the deepest level of nesting.
4. Finally, the function appends the calculated `nesting_level` for each chunk to the `result` list.

Note that this approach assumes that multiple groups of parentheses are separated by spaces, as reflected in the test case.

The unit tests passed. You can use this script to solve the problem statement. Feel free to modify it or add more test cases as needed.  If you have any more questions, corrections, or need additional assistance, feel free to ask!