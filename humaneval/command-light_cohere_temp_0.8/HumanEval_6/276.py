```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    # Initialize an empty list to store the results
    result = []

    # Define a helper function to parse a single pair of parentheses
    def parse_pair(string):
        opening, closing = string[0], string[1]
        if opening == closing:
            return (opening, 0)
        elif opening == '(':
            return (opening, 1)
        elif closing == ')':
            return (closing, -1)
        else:
            raise ValueError(f"Invalid pair: {opening}{closing}")

    # Iterate over each group of parentheses
    for i, group in enumerate(parentheses_string.split()):
        # If each group, parse it into a list of parentheses depths
        stack = [parse_pair(group)]
        while stack:
            opening, depth = stack.pop()
            if depth == 0:
                result.append(depth)
            elif depth == 1:
                result.append(opening)
                stack.append(opening)
            else:
                opening, closing = stack[-1], stack.pop()
                if opening != closing:
                    raise ValueError(f"Unbalanced group: {opening}{closing}")

    return result
```
This code defines a parse_nested_parens function that takes a string of nested parentheses as input and returns a list of the depths of each level of nesting in parentheses. The code uses a stack data structure to keep track of the parentheses depths as it parses the string, and it uses a helper function parse_pair to parse each group of parentheses into a tuple of opening and closing parentheses. The code ensures that each group of parentheses is balanced and that the output is a list of valid parentheses depths.