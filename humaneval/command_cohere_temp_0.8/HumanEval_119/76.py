```python
def match_parens(lst):
    def check(s, par):
        if not s:
            return True
        if par == 0:
            return False
        if s.endswith(')'):
            return check(s[:-1], par - 1)
        if s.startswith('('):
            return check(s[1:], par + 1)
        return False
    
    return 'Yes' if any(check(s, par) for s, par in zip(lst, itertools.count(0))) else 'No'
```

The function employs a recursive solution, but for technical limitations, please be aware that the maximum depth of recursion may be set to 128. So, with strings deeper than that, it won't give the expected answer, and you will get aRecursionError. But for most practical purposes, a depth of 128 is extremely large and unlikely to occur.

The `itertools.count(0)` is used as a iterator, with each iteration corresponding to a change in the parity (i.e., parity 0 for '(' and parity 1 for ')'). And the `zip` is used to iterate over each character of the string and its corresponding parity.