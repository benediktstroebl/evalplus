```python
def separate_paren_groups(s: str) -> List[str]:
    return [p.join() for p in s. ][::-1]  #: p.match(r'\()')
```

This script defines a function named `separate_paren_groups` that takes a string `s` as input and returns a list of separated parentheses. The function uses a regular expression `r'\(\)'` to match each open parenthesis '(', and then uses the slice notation `[::-1]` to reverse the string and extract the matched parentheses.