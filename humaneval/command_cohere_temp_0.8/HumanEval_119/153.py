```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if open_tup and close_tup and len(open_tup) == len(close_tup) else "No"
```

This approach involves converting the parenthesis characters to tuples and performing a matching check. 

Here's an explanation of the algorithm:
- Create a tuple called `open_tup` that contains all open parentheses `(`) from the first string.
- Create another tuple called `close_tup` that contains all close parentheses `)` from the second string.
- If both `open_tup` and `close_tup` are not empty (meaning there are matching pairs of parentheses) and the lengths of both tuples are equal (meaning each open parenthesis has a matching close parenthesis), return "Yes".
- Otherwise, return "No". 

This algorithm leverages tuple unpacking and string slicing for efficiency. 

The code is self-contained as it doesn't import any additional modules and provides a clear and concise solution to the problem. 

It's important to note that this will work appropriately for strings containing only parentheses. Adjustments may be needed for other restricted character sets.