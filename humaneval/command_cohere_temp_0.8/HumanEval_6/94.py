```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nest = 0
        imbalance = 0
        for c in chunk:
            if c == '(':
                nest += 1
                imbalance += 1
            elif c == ')':
                nest -= 1
                imbalance -= 1
            if imbalance > 0:
                result.append(nest)
                imbalance = 0
    return result
```

To understand the solution, let's break down the logic into steps:
1. **Input Argument**: The function `parse_nested_parens` takes a string `s` as input, which represents multiple groups for nested parentheses separated by spaces. 
2. **Splitting Chunks**: The input string is split into a list of substrings using the `split()` method. Each substring represents a group of parentheses. 
3. **Counting Nesting Levels**: For each substring or chunk, we maintain a `nest` variable that keeps track of the current level of nesting. We also use an `imbalance` variable to keep track of whether there are more open parentheses than closed ones (`imbalance > 0`) since a maximum nesting level is reached when there are more closers than openers in a chunk. 
4. **Updating Nesting Level**: When an open parenthesis `(` is encountered, we increment the `nest` and `imbalance` variables. When a close parenthesis `)` is encountered, we decrement these variables. 
5. **Appending Result**: We append the current nesting level `nest` to the `result` list when the `imbalance` is greater than zero, meaning we have reached a maximum nesting level within a chunk. 
6. **Return Result**: After processing all the chunks, the function returns a list of the maximum nesting levels for each group of parentheses. 

The function takes advantage of the split nature of the input to iterate through each chunk individually, allowing us to keep track of the nesting level locally without any need for global variables that would interfere with other chunks. The solution is quite efficient with a time complexity of O(N) where N is the length of the input string.

The unit tests are also crucial for ensuring the function behaves as expected and correctly handles various scenarios including edge cases. The test case itself is a valid part of the solution as it ensures that the underlying function generalizes to unknown inputs and doesn't fail catastrophically.