```python
def flip_case(string: str) -> str:
    return string.lower() if string.isalpha() else else("hello") else "Error: invalid input"

# Test cases
test_case = "hello"
assert flip_case(test_case) == "HELLO"

test_case = "Hello"
assert flip_case(test_case) == "HELLO"

test_case = "H4ll Ost"
try:
    assert flip_case(test_case) == "h4llOst"
except Exception as e:
    print(f"Error: {e}")

test_case = "hello world"
assert flip_case(test_case) == "hELLO wROld"
 ```  This Python script defines a function flip_case, which converts a given string to lowercase. The function uses string.isalpha() to check if the string is already in the desired case. It returns the string if it is valid. The script also includes several test cases to verify the correctness of the flip_case function.