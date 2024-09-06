```python
import hashlib

def string_to_md5(text: str) -> str or None:
    """
    Encrypts the string into MD5 and returns the result or None if the text is empty.
    """
    if text and text.strip():
        try:
            return hashlib.md5(text.encode()).hexdigest()
        except Exception as e:
            raise Exception(f"An error occurred while encrypting the string: {e}")
    else:
        return None

# Test Cases
def test_string_to_md5():
    cases = [
        ("Hello World", "3e25960a79dbc69b674cd4ec67a72c62"),
        ("", None),
        ("   ", None),
        ("ABC", "ABC"),
        ("123", "E7D28FC52E4B551C4E4BAA4BA7528AAC"),
    ]

    for text, expected in cases:
        result = string_to_md5(text)
        assert result == expected, f"For text '{text}'\nexpected: {expected}\nactual: {result}"

if __name__ == "__main__":
    test_string_to_md5()
```

The provided code uses the `hashlib` library to generate an MD5 hash. Text is first checked for empty strings and leading/trailing spaces, and if valid, the `hashlib.md5()` function is used to generate the hash. Any errors are caught and raised back to the caller. The test cases are designed to verify the correctness of the `string_to_md5` function against known outputs. 

To ensure code correctness, it is recommended to use similar tests to cover various scenarios and edge cases, such as empty strings, whitespace-only strings, and long texts.