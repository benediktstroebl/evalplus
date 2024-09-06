```python
def match_parens(lst):
    open_tup = tuple(map(count_parens, lst[0]))
    close_tup = tuple(map(count_parens, lst[1]))
    
    if max(open_tup) != max(close_tup):
        return "No"
    
    return "Yes"

def count_parens(s):
    return len(s) // 2
```
The `match_parens` function takes in a list of two strings, both consisting of open parentheses ('(') or close parentheses (')') only. It counts the number of open parentheses and close parentheses using the `count_parens` helper function, then compares the counts to determine if it's possible to create a balanced string by concatenating the two input strings in some order. If the maximum count of open and close parentheses isn't equal, it returns "No" since a balanced string cannot be formed. If the counts are equal, it returns "Yes," indicating a way to form a balanced string. 

This approach ensures that the function is self-contained, and the code is concise while providing a clear explanation of the solution logic.