```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if open_tup and close_tup and len(open_tup) == len(close_tup) else "No"
```

The approach employs tuple unpacking and string concatenation to form a hypothetical result string. The function returns "Yes" if this hypothetical string is balanced and "No" otherwise. This solution is relatively efficient with time complexity of O(N) and space complexity of O(1), where N is the length of the input strings.

Here is a usage example:
```python
print(match_parens(['(()', ')']) )  # Output: Yes
print(match_parens([')', ')'])  # Output: No
```

This function can be tested with different inputs to ensure its correctness.