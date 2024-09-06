```python
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of nested parentheses.

    Args:
        s (string): Input string with parenthesis groups.

    Returns: list of separated strings.
    """
    string): ['()', '(', ')', '(()', ')', '[]', '{}']
    """
    # Initialize an empty list to store the separated strings.
    results = []
    
    # Iterate through the string
    for i in range(0, len(s) - 1):
        if s[i] == '(' and s[i+1] == ')':
            results.append(s[i])
            s[i], s[i+1] = ' ', ''
        elif s[i] == '(':
            s[i] = ' ' + s[i] + ' '
        elif s[i] == ')':
            s[i] = ' ' + s[i] + ' '

    return results

# Unit tests
def test_separate_paren_groups():
    test_cases = [
        "()",
        "() ()",
        "()() ()()",
        "((()))",
        "() ( )  ",
        "() ()() ()",
        "(( )) (( ))"
    ]
    
    for case in test_cases:
        actual_result = separate_paren_groups(case)
        expected_result = [""] * 4
        assert actual_result == expected_result
        print(f"Test passed: {case} == {expected_result}")

# Main
if __name__ == "__main__":
    test_separate_paren_groups()
```
This Python script defines a function `separate_paren_groups` that takes a string `s` as input and returns a list of separated strings. It accomplishes thisator task of separating different groups of opening and closing parentheses in the input string. The `test_separate_paren_groups` function contains a collection of test cases that are used to verify the correctness of the `separate_paren_groups` function. 
The `if __name__ == "__main__":` condition ensures that the code inside this block is executed only when the script is run directly.