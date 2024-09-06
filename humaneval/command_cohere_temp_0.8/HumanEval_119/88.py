```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if len(open_tup) == len(close_tup) else "No"
```

The approach employed in the function `match_parens` involves transforming the given problem from one of finding a sequence of open and close parentheses that balances, into a problem of counting the number of open and close parentheses and determining if they are equitably numerous.

To accomplish this, the function first employs tuple mapping to aggregate the open parentheses characters `'('` and the close parentheses characters `')'` into tuples from each string. Subsequently, the function compares the lengths of these tuples. Owing to the fact that each parentheses pair must be balanced, if the lengths of both tuples are identical, then it's feasible to construct a balanced parentheses string by pairing each open parenthesis with the corresponding close parenthesis from the other string. Accordingly, the function returns "Yes" in such cases. On the other hand, if the lengths of the tuples differ, it will be impossible to construct a balanced parentheses string. In such scenarios, the function returns "No".

The function's utilization of tuple mapping and comparison of tuple lengths allows for an efficient resolution to the problem, devoid of the need for intricate algorithms like dynamic programming or backtracking.

This approach is highly efficient, with a time complexity of O(N) where N is the length of the input strings, which can help solve the given problem optimally.