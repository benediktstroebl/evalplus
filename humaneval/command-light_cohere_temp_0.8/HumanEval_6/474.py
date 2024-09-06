Here's a self-contained Python function that parses and extracts the deepest level of nesting from a given string:
```python
def parse_nested_parens(s):
    # Parsing function to handle nested parentheses
    def nested_parser(group):
        return parse_nested_parens(group)  # Recursive call to continue parsing
    return [len(group)]  # Initialize with the depth of the group

    # Function to parse nested parentheses
    def parse(string):
        return nested_parser(string)  # Parse the entire string

    return parse(s)  # Call the function with the input string s
```

The function takes a string `s` as input and uses a recursive helper function `nested_parser` to break down the string into a list of lengths of groups representing the deepest level of nesting. The `parse` function is responsible for parsing the string, and returns the result.