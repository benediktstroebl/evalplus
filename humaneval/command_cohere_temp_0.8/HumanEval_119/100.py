```python
def match_parens(lst):
    def shift(s):
        """
        Shifts the string s such that if it represents a valid parentheses sequence,
        the result will represent the same valid parentheses sequence but with
        all opening parentheses on the left, and all closing parentheses on the right.
        """
        res = []
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                while stack and stack[-1] != '(':
                    res.append(stack.pop())
                if not stack:
                    return None  # unbalanced
                stack.pop()
                res.append(c)
        while stack:
            res.append(stack.pop())
        return res
    
    # The following 2 lines are the key to solve this problem
    # They combine 2 strings with alternating opening and closing parentheses,
    #   such that the result will have all opening parentheses on the left, 
    #   and all closing parentheses on the right.
    # If the result is a valid string, the 2 given strings must have been balanced!
    return 'Yes' if len(shift(lst[0] + lst[1])) == len(shift(lst[0])) and len(shift(lst[1])) == len(shift(lst[1])) else 'No'
``` 

The function first shifts the strings such that they have all opening parentheses on the left and all closing parentheses on the right. 
If the resulting string is a valid string, the 2 given strings must have been balanced!
The overall time complexity is O(N^2) with N being the length of the 2 strings, with a single recursion in the shift function.

The space complexity is also O(N) because the 2 strings are concatenated in memory. It is a balanced recursion with a stack of at most N elements.