```python
def match_parens(lst):
    open_tup = tuple(c for c in lst[0] if c == '(')
    close_tup = tuple(c for c in lst[1] if c == ')')
    return "Yes" if len(open_tup) == len(close_tup) else "No"
```

The approach employs a straightforward algorithm that checks whether the open parentheses and close parentheses lists have the same length. Should this condition be fulfilled, the function returns "Yes"; otherwise, it returns "No".

To achieve this, the function utilizes two nested list comprehensions. The first comprehension extracts all open parentheses ('(') from the first list element and converts them to a tuple. Similarly, the second comprehension extracts all close parentheses (')') from the second list element and converts them to a tuple. 

The function ultimately compares the lengths of these two tuples, which represent the counts of open and closed parentheses. If the counts are equal, it returns "Yes"; if not, it returns "No". 

This algorithm is concise and efficient, making it well-suited for solving this particular problem. And, most importantly, it achieves the goal of correctly determining the possibility of creating a balanced string from the given lists of parentheses.