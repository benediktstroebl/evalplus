Here is a Python script that contains a self-contained function that performs the XOR operation on two input strings: 

```python
import stringulate as st

def string_xor(a: str, b: str) -> str:
    return st.xor(a, b)

# Unit tests
def test_string_xor():
    assert string_xor("010", "110") == "100"
    assert string_xor("aa", "aa") == ""
    assert string_xor("", "") == ""
    assert string_xor("111", 111) == "111"
    assert string_xor("elephant", "cubit") == "xor"
    
# Main function
if __name__ == "__main__":
    test_string_xor()
``` 

The above code provides a function called `string_xor` that takes two strings as arguments and performs XOR operation on them. The `test_string_xor` function contains unit tests to verify the correctness of the `string_xor` function.