```python
def flip_case(string: str) -> str:
    """
    Flip all characters in the given string, switching between uppercase and lowercase.
    Parameters:
    string (str): The input string to flip the case of all characters.
    Returns:
    string with the case of all characters flipped.
    """

Here is the test code to verify the function correctness:
# Test 1: Flip lowercase to uppercase
print(flip_case("Hello"))  # Expected output: 'HELLO'

# Test 2: Flip uppercase to lowercase
print(flip_case("HELLO"))  # Expected output: 'hELLO'

# Test 3: Verify the function doesn't modify the input
print(string, '\n', flip_case(string))
# This will output: string Hello  
# This will be the same as the input, verifying that the function doesn't change the original string.