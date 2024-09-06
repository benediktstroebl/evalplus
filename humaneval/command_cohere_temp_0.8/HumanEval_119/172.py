```python
def match_parens(lst):
    def shift_left(s):
        return s[:len(s) - len(re.sub(r'(\))+', r' \1', s))]

    return 'Yes' if all(shift_left(s) == s for s in lst) else 'No'
```

The function uses a generator expression alongside the `re` module to filter out unbalanced open parentheses sequences from each string in the list. It then checks if all strings are equal to their shifted versions, which indicates that they are balanced, and returns 'Yes' in this case. Otherwise, it returns "No" if any string contains an unbalanced sequence of open parentheses.