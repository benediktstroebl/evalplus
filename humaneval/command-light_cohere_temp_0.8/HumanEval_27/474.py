```python
def flip_case(string: str) -> str:
    return ''.join lower() + string.lower()
 string.

# Test case 1
test_flip_case("Hello")
# Expected output: HeLLo

# Test case 2
test_flip_case("hello")
# Expected output: hELLo

# Testcase 3
test_flip_case("world")
# Expected output: dlROW

# Testcase 4
test_flip_case("rt Mastor")
# Expected output: trStor MAStOR

# Testcase 5
test_flip_case("carry")
# Expected output: Carry

```
The function `flip_case` takes a string as input and returns a new string with the first letter of each word in lowercase and the rest of the letters in uppercase. This is a string is passed as an parameter to the function and returned. The tests are a simple input/output examples that demonstrate the functionality of the `flip_case` function.