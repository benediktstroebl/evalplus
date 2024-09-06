```python
def match_parens(lst):
    def shift(s):
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
            elif char == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    return 'Yes' if shift(lst[0] + lst[1]) else 'No'
```

The provided Python script offers a concise and effective solution to the problem of checking if two strings consisting of parentheses can be concatenated to form a balanced string. The `match_parens` function takes in a list of two strings, each containing only open or close parentheses, and returns a boolean value indicating the possibility of forming a balanced string through concatenation. The function relies on a nested `shift` function, which accurately keeps track of the balance of parentheses within a given string. The solution showcases Python's practicality and effectiveness in tackling programming challenges, providing an elegant answer in just a few lines of code.