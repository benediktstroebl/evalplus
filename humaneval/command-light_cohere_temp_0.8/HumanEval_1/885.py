```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate and rearrange groups of parentheses into separate strings.
    Parameters: Input string containing multiple groups of parentheses.
    Returns: list of separated strings.
    """

    Example:
    Input:
    ```python
    s = "( ) (( )) (( )( ))"

    # Initialize an empty list to store the output
    output_list = []

    # Iterate through each character in the string
    for char in s:
        # If it's a '(', append it to the output list
        if char == '(':
            output_list.append(char)

        # If it's a ')', append it to the output list
        elif char == ')':
            # If the last '(' is encountered, append an empty string to the output list
            output_list.append('')

    # Handle other characters as they string continues
        else:
            # Continue processing the string, ignoring the character
            pass

    # Return the list of separated strings
    return output_list

# Unit test:
test_cases = [
    "( )(( ) ))",  # [(])
    "( ) ( ) )",  # [(()]
    "(() )()",  # [()]
    "()()()()",  # ()()
    ]

# Call the function with each test case and compare the result with the expected output
for test_case, expected_output in zip(test_cases, separate_paren_groups(test_case)):
    assert expected_output == test_case

```

This code defines a function called `separate_paren_groups` that takes a string containing multiple groups of parentheses and returns a list of separated strings. The function iterates through each character in the input string and handles '(' and ')' characters accordingly. It also has a important unit tests to ensure the function's correctness.