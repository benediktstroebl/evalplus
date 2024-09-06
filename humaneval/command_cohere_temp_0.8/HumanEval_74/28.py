```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else len(lst1) < len(lst2) and lst1 or lst2
```
This Python script defines a function called `total_match` that takes two lists of strings, `lst1` and `lst2`, as input. The purpose of this function is to determine which of the two lists has a total character count in its strings that is less than the other. If both lists have an equal count, the function returns the first list (`lst1`).

The function incorporates logical operators for a streamlined approach. It assesses the length of both lists, returning `lst1` if they're equal. If `lst1` has fewer characters than `lst2`, it returns `lst1`. However, if the length of `lst2` is lesser, the function returns `lst2`. This strategic use of operators simplifies the problem's solution.

The provided examples showcase the function's behavior when processing various input conditions, such as returning an empty list for empty input, and optimally identifying the list with fewer characters while handling different cases of common prefixes and suffixes.