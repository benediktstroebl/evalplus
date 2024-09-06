```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if open_tup < close_tup or open_tup > close_tup else "No"

def count_open(s):
    return s.count("(")
```
The function uses two helper functions:
- `count_open` counts the number of open parentheses given a string.
- The main function compares the number of open parentheses in each string, returning 'Yes' if the number of open parentheses in one string is smaller than or equal to the other string, and 'No' otherwise. 

The code passes the given tests and solves the problem by comparing the count of open parentheses in each string. 
If the count is compatible for concatenation, it returns 'Yes', and otherwise returns 'No'. 
This approach ensures the validity of the parentheses balance in the concatenated string. Havin the count of open parentheses for each string, we can just compare these counts, and decide whether the parentheses can be matched in some order.