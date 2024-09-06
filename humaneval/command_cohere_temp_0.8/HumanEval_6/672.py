```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], ')')[::-1]:
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employs a counter (level) for each opening parenthesis encountered and decrements it for each closing parenthesis. A stack (stack) keeps track of the maximum depth of nested parentheses encountered during each group in the string. This method returns a list of these maximum depths for each group, which will be the final output. 

To better understand, let's break down the code step by step:
1. **Data Structures**: We use a `list`, `stack`, to maintain the state of nested parentheses, and a `counter`, `level`, to keep track of the current depth of nesting.
2. **Zip and Reversal**: The `zip('(()')[::-1]`, `')'[::-1]` pairing is used to iterate over the opening and closing parentheses in reverse order. This is done because we want to process the parentheses from the last one to the first in the string, and Python's `zip` function iterates over pairs in the order that they appear in the iterables passed to it. By reversing both the opener and closer iterables, we ensure that they are paired in the correct order.
3. **Iterating Over the String**: For each pair of opening and closing parentheses, we check if the current character is an opener (`if c == opener:`), we increment the `level` counter, meaning we've entered a deeper level of nesting. If it's a closer, we decrement the `level` counter, meaning we've exited a level of nesting.
4. **Keeping Track of Maximum Depth**: We maintain a result list to store the maximum depth of each group. Whenever the `level` counter is incremented, we append the current value to the stack. When the string is processed completely, the last value in the stack will be the maximum depth of nesting for the last group. This value is appended to the `result` list.

You can test this function by calling it with different strings and comparing the results with the expected output.