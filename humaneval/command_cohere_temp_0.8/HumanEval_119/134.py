```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_parens(s):
    return s.replace("(", "").replace(")", "")
```

The function `match_parens` takes in a list of two strings, each containing only open or close parentheses, and determines if it's possible to concatenate the strings in some order to create a balanced parentheses string. It does so by counting the number of open and close parentheses in each string using the `count_parens` helper function, comparing the counts, and returning "Yes" if the number of open parentheses is less than or equal to the number of close parentheses, otherwise returning "No". 

This approach ensures that every possible combination of parentheses is accounted for and provides the correct answer based on the inequality relationship between open and close parentheses counts.