```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string of parenthesis-enclosed groups as its input and
    returns a list of separated strings.

    It reads the by starting at the beginning of the string, 
    moving forward until it encounters a close parenthesis, 
    and recording the match as a string.
    Returns: list of separated strings.
    """
code
    ```
    def separate_paren_groups(s: str) -> List[str]:
        # List to store separated strings
        res = []
        # Loop through the string, and at each step, check if it's a closing parenthesis 
        # If it is, append the current string to the result list, and skip the rest of the string
        # If it isn't a closing parenthesis, append the current character to the string 
        # for the next iteration 
        for i, char in enumerate(s):
            if char == ')':
                res.append(s[pop])
                s = s[i+1:]
            else:
                s = s[i]
        return res
    # Test cases
    test_cases = {
        "() (( )() )": ["()", "()", "()()"],
        "((()))" : ["()", "()", "()"],
        "()()()()": ["()", "()", "()"]
        # Add more test cases here
    }
    for case, expected in test_cases.
        got = separate_paren_groups(case)
        print(f"Case: {case}")
        print(f"Expected: {expected}")
        print(f"Got: {got}")
        assert got == expected
    ``` 
This script defines a function `separate_paren_groups` that takes a string of parenthesis-enclosed groups as input and returns a list of separated strings. The function uses a loop to separate the strings based on the presence of closing parenthesis, and the `res` list is used to store the separated strings. 
The script also includes a set of test cases to verify the function's correctness. 
Feel free to add more test cases to further validate the function.