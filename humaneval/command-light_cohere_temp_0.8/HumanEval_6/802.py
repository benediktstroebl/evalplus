Here is a self-contained Python script that solves the problem you have described:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s.matches(re.compile(r'(\)) + r'\(+\))', 'g'):
        stack.append(match.pop()  #inner)
    match.
    while stack and not [] and len(stack) == 1:
        group = stack.pop()
        format = group[1:-1].replace(')', '')
        if format == '(':
            result.append(1)
        else:
            result.append(len)
    return result
```

This code defines a function called **`parse_nested_parens`** that takes a string of text as input and returns a list of its deepest levels of nesting of parentheses. The code uses the regular expression **`(\)) + `** or `\(`)+`** to match each group of parentheses, and uses the **`pop()`** function to remove the deepest parentheses from the stack.

Finally, the code returns the list of deepest levels of nesting of parentheses.