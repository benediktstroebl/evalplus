```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    return "Yes" if open_tup <= close_tup else "No"

def count_open(s):
    return s.count("(") if s else 0
```
The approach involves mapping over each string in the list to count the number of open parentheses, which returns a tuple of counts. Subsequently, the logic checks if the tuple of counts for the open parentheses can be fully consumed by the tuple of counts for the close parentheses, implying a valid combination for a balanced string, hence the output is adjusted accordingly. 

This algorithm has a time complexity of O(nm) as it requires mapping over each character in both strings, and mapping over strings of length n takes O(n) time, leading to an overall complexity of O(nm).