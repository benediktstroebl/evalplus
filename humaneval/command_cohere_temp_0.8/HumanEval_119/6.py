```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    
    if max(open_tup) != max(close_tup):
        return 'No'
    
    return 'Yes'

def count_open(s):
    open_cnt = s.count('(')
    close_cnt = s.count(')')
    return open_cnt - close_cnt
```

The approach involves:
- Creating tuples of open counts and close counts for both input strings.
- Checking if the maximum open count is equal to the maximum close count. If not, this assures that the two strings cannot create a balanced string, so the answer is 'No'.
- If the maximum counts are equal, this guarantees there is at least one ordering of the strings that creates a balanced result, thus returning 'Yes'.