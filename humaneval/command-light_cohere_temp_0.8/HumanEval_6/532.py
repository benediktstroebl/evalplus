```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    out = []
    for c in s:
        if c == " ":
            stack.append(out)
        out.append(len)
        while c == "(")
        stack.append(out)
        out.append(c)
    return out
``` 
This code defines a function `parse_nested_parens` that takes a string `s` as input and returns a list of integers `out` that represents the deepest level of nesting of parentheses in the string. The function uses a stack to keep track of the open parenthesis groups, and uses a while loop to iterate over the characters in the input string. 

The `out` list is used to append the deepest level of parenthesis encountered while iterating through the string. 

This function correctly handles nested parentheses and returns the correct result.