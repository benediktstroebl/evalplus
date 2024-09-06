```python
def match_parens(lst):
    close = ')'
    for open in lst:
        if open != close:
            balance = 0
            s = open + close
            while s:
                if s.count(open) > s.count(close):
                    return "No"
                balance += s.count(open) - s.count(close)
                s = s[:-1]
            if balance == 0:
                return "Yes"
    return "No"
```

This code defines a function `match_parens` that takes a list of strings as input and aims to determine if it's possible to concatenate these strings in some order to create a balanced string of parentheses. The function iterates through the provided list and attempts to match pairs of opening and closing parentheses. It maintains a count of the balance of parentheses as it iterates through the string. If the balance is zero at the end, it returns "Yes," indicating a possible way to create a balanced string. Otherwise, it returns "No" since there are no matching pairs, and a balanced string cannot be formed.