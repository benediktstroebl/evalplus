```python
def parse_nested_parens(parenthes_string: str) -> List[int]:  # Function to parse nested parentheses
    def get_parentheses_level(match):  # Helper function to get the level of the deepest matching parentheses
        return len(match.group())  # Match object from regex matches

    match = regex_pattern.match(parenthes_string)
    if match:
        return get_parentheses_level(match)
    else:
        raise ValueError("Parentheses not found")

    return []

parentheses_input = """(())(()())((()))()((())()())""
 parsed_level = parse_nested_parens(parentheses_input)
print(f"Deepest level of parentheses: {parsed_level}")  # Should print 3
```
The provided Python script defines a function parse_nested_parens that takes a string as input and aims to determine the deepest level of nesting for parentheses in the string. Additionally, it employs a custom approach that involves the use of regular expressions and a helper function get_parentheses_level to extract the level of the deepest parentheses from a match object. The script also includes a sample test string and executes the function to calculate and print the deepest level of parentheses detected.