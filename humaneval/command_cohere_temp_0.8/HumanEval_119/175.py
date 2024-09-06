```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    if max(open_tup) == max(close_tup):
        return "Yes"
    return "No"

def count_open(s):
    open_cnt = s.count("(")
    close_cnt = s.count(")")
    return open_cnt - close_cnt
```

The approach uses a simple algorithm that checks if the counts of open parentheses ('(') in both strings are equal to the counts of closed parentheses (')') in them. The function counts the number of open parentheses in each string and subtracts the number of closed parentheses to calculate the net number of open parentheses. If the max count of open parentheses in both strings is equal, it returns "Yes" since we can merge the strings in some order to have a balanced number of open and closed parentheses. If the max count differs, it returns "No" as there is no way to concatenate the strings to obtain a balanced string. 

The code may fail for strings that exceed the maximum recursion depth in the Python interpreter, i.e., for extremely unbalanced parentheses, you may consider using a different approach.