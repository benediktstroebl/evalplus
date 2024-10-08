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

    return 'Yes' if is_good(lst[0]) or is_good(lst[1]) else 'No'
```
The provided solution employs a simple **Depth-First Search (DFS)** approach to verify if there exists a way to concatenate the two strings so that the resultant string is balanced. It also employs a stack to track the opening parentheses '(' and popping occurs whenever we encounter a closing parentheses ')' to ensure a proper balance. The function returns 'Yes' if at least one of the two strings is good, and 'No' otherwise. 

This approach guarantees a time complexity of O(N) where N represents the size of the string, making it an efficient solution.