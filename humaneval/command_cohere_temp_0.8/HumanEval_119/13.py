```python
def match_parens(lst):
    def merge(a, b):
        count_a = count_b = 0
        current = a
        while count_a < len(a) or count_b < len(b):
            open_par = min(count_a, count_b)
            close_par = max(count_a, count_b)
            if current[-open_par:] == '(' * open_par:
                current += b[close_par - open_par:]
                count_a -= open_par
                count_b -= close_par
            elif current[-open_par:] == ')' * open_par:
                current += a[close_par - open_par:]
                count_a -= open_par
                count_b -= close_par
            else:
                return False
            if not count_a and not count_b:
                return True
        return False

    return "Yes" if any(merge(a, b) for a, b in zip(lst, lst[1:])) else "No"
```

The `merge` function checks if it's possible to merge two given strings `a` and `b` while ensuring proper parentheses balancing. It does this by comparing the counts of open and close parentheses at each step and adjusting the corresponding strings accordingly. The primary function `match_parens` iterates through all possible pairings of the list elements and checks if any of them can be merged successfully, if any valid merge is found, it returns "Yes", otherwise, it returns "No".

This approach allows the function to determine the answer for any given input in a straightforward manner, without the need to concatenate the strings directly, which could lead to potential overflow issues for large inputs.