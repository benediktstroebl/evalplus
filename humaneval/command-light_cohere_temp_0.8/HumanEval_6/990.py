```python
def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting for a given string of parentheses.
    Args:
        paren_string (str): The string containing multiple groups of parentheses separated by spaces.
    Returns:
        list[int]: A list of the deepest level of nesting for each group of parentheses.
    """
    example:
    Input: "(()()) ((())) () ((()))"
    Output: [2, 3, 1, 3]
    """
    # Define a helper function to find the deepest level of nesting for each group of parentheses
    def deepest_level(parentheses: str) -> List[int]:
        stack = []
        opening_parens = []
        closing_parens = []
        for parantype in parentheses:
            if parantype.count( ) == 1:  # if its only one character
                stack.append(1)
                else:  # if its closing parent, add it to closing_parens list
                closing_parens.append(stack.pop()
                -open(stack) + [stack.pop() for i in range(stack) if stack[i] == 1])
            stack.append(0)  # if its opening parent, add it to stack list
            opening_parens.append(stack.pop() for i in range(stack) if stack[i] == 0))
        return opening_parens

    # Example usage
    input_str = "(()()) ((())) () ((()))"
    deepest = deepest_level(input_str)
    print(deepest)
    ```