```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], ')':
        stack = [0]
        for ch in s:
            if ch == opener:
                stack.append(stack[-1] + 1)
            elif ch == closer:
                stack.pop()
        result.append(stack[0])
    return result
```

The Python script provided defines a single function, `parse_nested_parens`, which takes a single argument, `s`, representing a string of nested parentheses. This function is designed to solve the problem of computing the deepest level of nesting of parentheses in each group, as described in the problem statement.

Here's a step-by-step description of how the function works:
1. **Type Definition**: The function starts by importing the `List` module from the `typing` module. This is optional but helps provide meaningful type annotations for the function.
2. **Function Definition**: The `parse_nested_parens` function is defined with a single parameter, `s`, which represents the input string of nested parentheses. The return type of this function is specified as a list of integers.
3. **Loop for Opening and Closing Parentheses**: The core of the function is a loop that iterates through the opening parentheses ('(') and closing parentheses (')'/). The loop runs in reverse, from the last opening parenthesis to the first closing parenthesis, using the `zip('(()')[::-1]` mechanism.
4. **Initialization of Result and Stack**: For each pair of opening and closing parentheses, the function initializes an empty list `stack` to keep track of the nesting level. The `result` list is also initialized with an empty list to store the final result.
5. **Iterating Through the String**: The function then iterates through each character in the input string `s`.
    - If the character is an opening parenthesis, the function appends the current nesting level plus one to the `stack`. This is done because each opening parenthesis increases the nesting level.
    - If the character is a closing parenthesis, the function pops the top element from the `stack`. This simulates reducing the nesting level by one when a closing parenthesis is encountered.
6. **Appending Result**: After processing all characters, the function appends the final nesting level (the top of the stack) to the `result` list.
7. **Return the Result**: Finally, the function returns the `result` list, which contains the deepest level of nesting for each group of parentheses in the input string.

The function utilizes a stack-like data structure (the `stack` list) to keep track of the current nesting level as the input string is processed. The reversed iteration of opening and closing parentheses ensures that the deepest level of nesting is computed correctly even in cases of overlapping parentheses.

To test the function, you can use the provided test case in the problem statement, and the function should return the expected output `[2, 3, 1, 3]`.