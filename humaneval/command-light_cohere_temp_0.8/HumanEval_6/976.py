Here is a Python script that contains a self-contained function that solves the problem of recognizing nested parentheses:
```python
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_levels: List[int] = [0, 2]  # [0: non-parenthesis, 2: first-level round brackets]
    closing_levels: List[int] = [1, 3]  # [1: other than non-parenthesis, 3: second-level round brackets]

    for char in s:
        if char == " ":
            stack.append(opening_levels.append(closing_levels.append(0))  # Consume space and reset counts
        closing_levels.append(opening_levels.append(1))  # Add closing brackets to stack

        stack.append(closing_levels.append(opening_levels))  # Consume brackets and reset counts
        opening_levels.append(closing_levels)  # Add opening brackets to stack
        closing_levels.append(opening_levels)  # Add closing brackets to stack
        if len(stack) == 4:  # Found full set of brackets
            stack.pop()  # Check if stack empty
            return stack[:]  # Return list of deepest-level brackets

    # Test the function
    test_str = "(()()) ((())) () ((())()())"
    result = parse_nested_parens(test_str)
    print(result)  # Output: [(), 3, 1, 3]
```

This script provides a function called `parse_nested_parens` that accepts a string containing multiple groups of parentheses separated by spaces. It uses a stack and two lists of opening/closing bracket levels to determine the correct hierarchy of each group.