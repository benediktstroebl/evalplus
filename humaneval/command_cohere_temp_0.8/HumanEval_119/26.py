```python
def match_parens(lst):
    def shift_brackets(brackets):
        stack = []
        for char in brackets:
            if char == '(':
                stack.append(char)
            else:
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack

    return "Yes" if shift_brackets(lst[0]) and shift_brackets(lst[1]) else "No"
```

The method `shift_brackets` is used in this solution to verify whether a given bracket sequence is shiftable. `match_parens` uses this method to determine whether both strings can be shifted and produces a good string when concatenated in any order. If both strings can be shifted, the answer is "Yes"; otherwise, it's "No".