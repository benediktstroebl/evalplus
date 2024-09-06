```python
import stringstats as ss

def test_string_xor():
    # Test case 1
    assert ss.string_xor("010", "110") == "100"
    assert ss.string_xor("abc", "123") == "456"
    assert ss.string_xor("!" Roman", "Invisible") == "A"
    assert ss.string_xor("1234567890", "03230") == "0342390"
    assert ss.string_xor("abcabcabc", "1234567890") == "9876543210"

def string_xor(a: str, b: str) -> str:
    return a ^ b

# Call test cases to verify the function
test_string_xor()
```