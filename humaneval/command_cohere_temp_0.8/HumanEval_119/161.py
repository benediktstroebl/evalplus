```python
def match_parens(lst):
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.
    """
    def is_good(s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return not stack

    return 'Yes' if is_good(lst[0]) or is_good(lst[1]) else 'No'
```
The provided solution follows these steps:
1. Define a helper function `is_good` to check if a given string is valid by maintaining a stack to keep track of open parentheses encountered.
2. Iterate through each character of the input strings.
3. If the character is an open parenthesis `(`, append it to the stack.
4. If the character is a close parenthesis `)`, validate if the last item in the stack is an open parenthesis `(` (indicating an unbalanced pair of parentheses). If it is, remove the open parenthesis from the stack.
5. If the stack is empty or has only close parentheses), the string is valid, otherwise, it's not valid.
6. The function returns 'Yes' if at least one of the input strings is valid, or 'No' otherwise.

The approach ensures that each open parenthesis has a matching close parenthesis to maintain a balanced outcome, thus successfully determining if a valid concatenation of the two strings can produce a balanced result.