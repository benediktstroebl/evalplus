```python
def match_parens(lst):
    return 'Yes' if any(balance_parens(s) for s in lst) else 'No'
    
def balance_parens(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0: return False
    return count == 0
```
The provided code first uses the any function to check if either of the strings in the input list has balanced parentheses. If neither string has balanced parentheses, it returns 'No'. Otherwise, it returns 'Yes'. 

The function `balance_parens` correctly maintains a count of open parentheses encountered and ensures that each open parenthesis is matched with a close parenthesis. It returns True if the string has balanced parentheses and False otherwise.