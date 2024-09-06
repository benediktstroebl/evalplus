Here's a self-contained Python function that parses and deepest-level parentheses in a string:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    result = []

    for char in s:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(char)
                stack.push(0)
            else:
                result.append(stack.pop())
   }char) return
   
```

This function, `parse_nested_parens`, takes a string `s` as input and returns a list of integers. It works by iterating each character in the string and maintaining a stack of opening parentheses. The function then appends the appropriate character to the list depending on the character. Finally, it returns the list of integers, where the first element is the character that was last added to the stack, and the remaining elements are the deepest level of nesting of parentheses in the string.