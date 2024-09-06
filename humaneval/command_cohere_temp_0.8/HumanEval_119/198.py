```python
def match_parens(lst):
    open_tup = tuple(map(count_open, lst[0]))
    close_tup = tuple(map(count_open, lst[1]))
    return 'Yes' if len(open_tup) == len(close_tup) and all(open == close for open, close in zip(open_tup, close_tup)) else 'No'

def count_open(s):
    return s.count('(') - s.count(')')
```

The function relies on two nested helper functions:
1. `count_open(s)`: This function assesses the number of open parentheses `(`) versus closed parentheses `)`. It's an alternating string, so the count should be the same.
2. `open_tup = tuple(map(count_open, lst[0]))`: This snippet calculates the number of open parentheses for each string in the provided list. It maps the `count_open` function to each string, and the result is aggregated into a tuple.

The main logic then checks if the lengths of `open_tup` and `close_tup` are equal and whether they contain balanced parentheses. The result is then returned as 'Yes' or 'No'.