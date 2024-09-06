```python
def match_parens(lst):
    cnt_open = 0
    for el in lst:
        if el == '(':
            cnt_open += 1
        else:
            cnt_open -= 1
        if cnt_open < 0: return "No"
    return "Yes"
```
The function performs the task using a counter of open parentheses `cnt_open` which is increased whenever an open parenthesis `(` is encountered and decreased when a close parenthesis `)` is encountered. The function returns `"No"` if the counter is negative at any point, indicating an unbalanced string, and `"Yes"` otherwise. This approach allows the function to determine if a concatenation of the two strings in any order will result in a balanced string.