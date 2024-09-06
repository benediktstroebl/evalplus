```python
def match_parens(lst):
    def shift_brackets(brackets):
        stack = []
        for bracket in brackets:
            if bracket == '(':
                stack.append(bracket)
            else:
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack

    return "Yes" if shift_brackets(lst[0]) and shift_brackets(lst[1]) else "No"
```

The method `shift_brackets` is used here to verify whether it is possible to concatenate the two strings in some order to create a balanced parentheses string. This method accepts a string of brackets as input and outputs `True` if the brackets are balanced (`(()`) or unbalanced (`())`).

The main function `match_parens` uses this method to determine if the two strings can be concatenated to form a balanced parentheses string, and returns "Yes" if possible and "No" otherwise. 

This approach has a time complexity of O(n) where `n` is the length of the string, since it checks each character once. It has a space complexity of O(k) where `k` is the maximum depth of the recursion stack, but since this is a bounded constant for any valid input size, we ignore this complexity.