Here's a self-contained Python script with a function that parses and explodes nested parentheses in markdown code blocks:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    level = 0
    in_string = False  # Track if we are inside a string
    output = []  # Resultant list of levels of nesting

    for char in s:
        if char == " ":
            if in_string:
                stack.append(level)
                level += 1
            in_string = False  # Clear out the current string state
        else:
            in_string = True  # Start a new string state

        if char == ")":
            stack.append(level)
        level = 0  # Reset after opening parenthesis

        if len(stack) > 1:  # More than one level of nesting, so we have a nested group
            output.append(stack.pop())  # .  # Explode nested list

    return output  # Return the list of levels of nesting
```

This script defines a function `parse_nested_parens` that takes a string as input and returns a list of integers representing the levels of nesting. The function uses a stack data structure to keep track of the levels of nesting, and it uses a level counter to track the depth of the current group of parentheses. The function also uses a `in_string` flag to track whether we are inside a string and uses this flag to reset the level counter and clear out the string state after the opening of a parenthesis.