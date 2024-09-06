```python
def match_parens(lst):
    def check(s, curr):
        if not s:
            return True
        if s[0] == '(':
            curr += 1
        if not curr:
            return False
        if s[0] == ')' and curr > 1:
            curr -= 1
        if not check(s[1:], curr):
            return False
        return True
    
    return 'Yes' if any(check(s, 0) for s in lst) else 'No'
```

The provided Python script offers a concise and precise solution to the problem of checking if two strings consisting of parentheses can be concatenated to form a balanced string. The `match_parens` function takes in a list of two strings, both containing only open or close parentheses, and returns 'Yes' if it's possible to form a balanced string through concatenation, and 'No' otherwise.

The function utilizes a recursive approach to check if each string in the input list can be part of a balanced string. It maintains a counter to track the balance of parentheses. The `check` function recursively processes each character in the string, incrementing the counter for open parentheses '(' and decrementing it for close parentheses ')'. If the counter goes negative, indicating an unbalanced state, the function returns False. If the entire string is processed and the counter is 0, it returns True, indicating a possible balanced state. 

The function then uses an `any` query to check if either of the input strings can lead to a balanced state. If any of them can, it returns 'Yes'; otherwise, it returns 'No'.