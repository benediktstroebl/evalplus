```python
import stringcase as tc

# Function to perform XOR operation on two strings consisting only of digits
def string_xor(a: str, b: str) -> str:
    """
    XOR two strings containing only digits
    Parameters:
        a (str): Input string (can contain only digits)
        b (str): Input string (can contain only digits)
    Returns: str: Result of XOR operation on a and b
    """
    if not (tc.isalpha('a', 'b')):
        raise ValueError("Input strings a and b must contain only digits")

    return tc.join(a, b, 'xor')
```

The function takes two strings as parameters, and returns the XOR operation of the two strings. This is result is always a string.

The function includes a test to ensure that the input strings contain only digits. If the input does not pass this test, a ValueError is raised. 

The test uses the tc.alpha() function to check if the strings contain only letters or digits, and returns True if they do, and False otherwise. 

It performs the XOR operation on the two strings using the tc.join() function, and returns the result as a string.