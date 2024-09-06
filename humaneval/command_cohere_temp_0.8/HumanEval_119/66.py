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
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if not stack or stack.pop() != '(':
                    return False
                else:
                    stack.pop()
        return not stack

    return 'Yes' if is_good(lst[0] + lst[1]) or is_good(lst[1] + lst[0]) else 'No'
```
The provided solution follows these steps:
1. Define a helper function `is_good` to check if a given string is valid by iterating through its characters and maintaining a stack to track open parentheses.
2. If the list has two strings, `a` and `b`, the main function checks if either `a` followed by `b` or `b` followed by `a` results in a good string using the helper function.
3. If neither concatenation leads to a valid string, the function returns 'No'; otherwise, it returns 'Yes'. 

This approach allows the function to efficiently determine the validity of the concatenated strings and provide the appropriate outcome.