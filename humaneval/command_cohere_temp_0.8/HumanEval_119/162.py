```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    if max(open_tup) != max(close_tup):
        return 'No'
    return 'Yes'
    
def count_open(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
    return balance
```
The code uses two functions: `count_open` to count the number of open parentheses encountered as we iterate through a given string `s`, and `match_parens` acts as an adapter to the original problem statement. The `match_parens` checks the number of open parentheses in each string, and returns 'Yes' if these counts are equal, and 'No' otherwise. These correspond to the maximum number of open parentheses in either string: if one string has a different count of open parentheses, they cannot be concatenated in any order to result in a balanced parentheses string.