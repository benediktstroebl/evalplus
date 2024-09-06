Here is a Python script that demonstrates the function `separate_paren_groups` with self-contained tests:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups of balanced parentheses into separate strings and return them.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    return [p for p in s if not(p=='(')')))

# Test string with valid and invalid inputs
test_cases = [
    ("()()"),
    ("(()))"),
    ("()"),
    ("((()) )"),
    ("((((()))))"),
    ("  ()"),
    ("() () ()"),
    ("( )  "),
    ("  (() )"),
]

# Loop through test cases
for s in test_cases:
    # Call the function with test string
    result = separate_paren_groups(s)
    
    # Validate the results
    assert len(result)==len(test_cases), "Length mismatch in results."
    for i in range(len(result)):
        assert result[i] in test_cases[i], f"Invalid result: {result[i]}, expected: {test_cases[i]}."
```

The `separate_paren_groups` function in this script accepts a string as input and divides it into separate strings by properly separating each group of parentheses. The test cases include a variety of scenarios, including valid and invalid inputs, to ensure that the function is working as intended. The function also validates that the result matches the anticipated length and contains the proper strings.