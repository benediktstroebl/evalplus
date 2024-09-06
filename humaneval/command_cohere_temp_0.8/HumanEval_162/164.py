```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string to its MD5 hash and handles empty strings gracefully.

    Args:
        text (str): The input string.

    Returns:
        str or None: The MD5 hash of the input string if it's not empty, otherwise None.
    """
    if text:
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None

# Test scenarios and expected outputs
test_scenarios = [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("", None),
    ("   ", None),
    ("ABC", "ABC"),
]

for text, expected in test_scenarios:
    result = string_to_md5(text)
    if result != expected:
        print(f"Test failed for input '{text}'. Expected {expected}, got {result}.")
    else:
        print(f"Test passed for input '{text}'.")
```

The provided code snippet performs the following:
1. It imports the `hashlib` module, which supplies interfaces to many hash and message digest algorithms, including the MD5 algorithm.
2. The `string_to_md5` function accepts a text string as an argument.
3. If the text argument is not empty, the function employs the `hashlib.md5()` function to generate the MD5 hash of the text. The `encode()` method is used to convert the text into bytes since the `hashlib.md5()` function expects bytes-like input. Then, `.hexdigest()` is used to return the hexadecimal representation of the hash.
4. If the input text is empty, the function returns None. This is to accommodate the problem's statement, which states that the function should handle empty strings gracefully.
5. The script then presents a series of test scenarios with accompanying expected outputs. These scenarios validate the correct behavior of the `string_to_md5` function.
6. For each test scenario, the function is invoked with the text, and the result is compared with the expected output. If the values don't match, a failure message is displayed. 
7. When the values match, a pass message is displayed, indicating that the test scenario's result was as expected. 

This comprehensive approach ensures that the function behaves correctly in multiple contexts and aligns with the problem's expected output.  Any discrepancy between the expected output and the actual result would lead to a test failure notification, enabling easy identification of issues.  This enables the easy identification of issues.