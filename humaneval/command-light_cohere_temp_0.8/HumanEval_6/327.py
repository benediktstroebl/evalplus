Here's a self-contained Python script with a function that solves the problem of parsing and recognizing nested parentheses:
```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []

    for char in parentheses_string:
        if char == ")":
            stack.append(len)
        if char == "(":
            stack.append(1)
        result.append(stack.pop())
        if char != ")":
            stack.pop()

   if char != "("
            stack.append(1)

    return result
```

This script defines a function `parse_nested_parens` that takes a string of parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses in the string. 

It uses a stack data structure to keep track of opening parentheses and their nesting levels. The function iterates through each character in the input string, and uses a series of if-elif statements to determine the depth of the current group of parentheses and add it to the `result` list. 

Finally, the function returns the `result` list, which contains the deepest levels of nesting for each group of parentheses in the string.