```python
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses and returns the deepest level of nesting for each group.
    Args:
        parent_string (str): The string to parse for the level of nesting.
    Returns:
    list[int]: A list of integers where each integer represents the deepest level of nesting.
    """
    sample usage:
    nested_paired = parse_nested_parens('(()()) ((())) () ((())()())')
    print(nested_paired)
    ```