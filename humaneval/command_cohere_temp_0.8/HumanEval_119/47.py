```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if len(open_tup) == len(close_tup) else "No"
```

The approach employs a simple algorithm that directly matches open parentheses with close parentheses. The function correctly determines if the two strings can be concatenated to form a balanced string. 

#### Complexity Analysis:
The time complexity of the algorithm is: `O(min(M, N))`, where `M` is the length of the first string and `N` is the length of the second string. This is because the algorithm iterates over each character in the strings, and in the worst case, the algorithm would iterate over the shorter of the two strings. 

The space complexity is: `O(1)`, since the algorithm uses a constant amount of space to store the iterated characters in tuples.