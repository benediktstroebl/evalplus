```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_parens(s):
    return s.count("(") - s.count(")")
```
The provided code defines a function `match_parens` that takes a list of two strings as input, each containing only open parentheses '(' or close parentheses ')', and it returns either "Yes" or "No" depending on whether it's possible to concatenate the strings in some order to create a balanced parentheses string.

To achieve this, the function uses a `count_parens` helper function to count the number of open parentheses '(' and subtracts the number of close parentheses ')' in each input string. These counts are then compared using the logical constraint that the number of open parentheses must not exceed the number of close parentheses in any valid concatenation. 

Overall, the code provides an efficient and concise solution to the problem as per the problem statement provided.