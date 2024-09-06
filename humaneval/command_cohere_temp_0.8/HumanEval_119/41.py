```python
def match_parens(lst):
    def check(s, br):
        if len(s) != len(br):
            return False
        cnt = 0
        for char in s:
            if char == '(':
                cnt += 1
            elif char == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0
    
    return 'Yes' if any(map(check, lst)) else 'No'
```

This code defines a function `match_parens` that takes a list of strings as input and returns 'Yes' if it's possible to concatenate the strings in some order to create a balanced parentheses string, and 'No' otherwise. It introduces a helper function `check` to calculate the balance of a particular string, then checks if any of the provided strings has a balanced parentheses count.