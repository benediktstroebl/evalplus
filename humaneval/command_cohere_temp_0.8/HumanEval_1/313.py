Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of separate groups of parentheses. The code is structured to provide test coverage for the function:
```python
# Importing type hinting module
from typing import List

# The function to be tested
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    # Define an empty list to store the separate groups of parentheses
    output: List[str] = []

    # Define a stack to store the opening parentheses encountered
    stack: List[str] = []

    # Iterate over each character in the input string
    for char in paren_string:
        # If the current character is an opening parenthesis
        if char == '(':
            # Add it to the stack
            stack.append(char)
        # If the current character is a closing parenthesis
        elif char == ')':
            # If the stack is empty, this closing parenthesis corresponds to the last opening parenthesis
            if not stack:
                continue
            # Pop the top element from the stack, which is the corresponding opening parenthesis
            opening_char = stack.pop()
            # If the opening parenthesis was not ')(' (i.e., it was '('), add the current closing parenthesis to the output
            if opening_char != '(':
                output.append(char)
        # If the current character is a space, it should be ignored
        elif char == ' ':
            continue
        # In any other case, something unexpected is happening
        else:
            raise ValueError("Encountered an unexpected character. Expected only parentheses and spaces.")

    # If the stack is not empty at the end of the loop, this means there are unclosed parentheses
    if stack:
        raise ValueError("Encountered unclosed parentheses.")

    # Return the list of separated groups of parentheses
    return output


if __name__ == "__main__":
    # Sample input and expected output
    import unittest

    class TestSeparateParenGroupsFunction(unittest.TestCase):
        def test_empty_string(self):
            self.assertEqual(separate_paren_groups(""), [])

        def test_single_group(self):
            self.assertEqual(separate_paren_groups("()"), ["()"])

        def test_multiple_groups(self):
            self.assertEqual(separate_paren_groups("( ) (( )) (( )( ))"), ["()", "(())", "(()())"])

        def test_unbalanced_groups(self):
            with self.assertRaises(ValueError):
                separate_paren_groups("(()")

        def test_nested_groups(self):
            with self.assertRaises(ValueError):
                separate_paren_groups("((()))")

        def test_unexpected_characters(self):
            with self.assertRaises(ValueError):
                separate_paren_groups("( a ))"))

    if __name__ == "__main__":
        unittest.main()
```

This code provides test coverage for various scenarios, including edge cases, and checks if the `separate_paren_groups` function behaves as expected.