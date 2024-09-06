Here is a Python script with a self-contained function that solves the problem of finding the deepest level of nesting of parentheses in a given string:
```python
def parse_nested_parens(string):
    """
    Finds the deepest level of nesting for parentheses in a given string.
    Args:
        string (str): string to check for nested parentheses.

    Returns:
    list of depths of nesting for each group of parentheses in str.
    """
    def find_level(string):
        stack = []
        level = 0
        in_parens = False
        for char in string:
            if char == "(" and not in_parens:
                in_parens = True
                stack.append(level)
                level += 1
            elif char == ")" and in_parens:
                in_parens = False
                stack.pop() if stack:
                    return [stack][-1]
        return []
    return find_level(string)
```
This function takes a string `string` as input and iterates through each character. It uses two nested stack data structure to keep track of the nesting level. It also uses an "in_parens" flag to differentiate between the opening and closing of parentheses. 

The function returns a list of depths of nesting for each group of parentheses in the string.