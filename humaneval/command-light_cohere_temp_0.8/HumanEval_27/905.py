```python
def flip_case(string: str) -> str:
    new_str = ""
    for c in string:
        if c.isalpha():
            new_str += c.isUcs() and + c.isLower() and
           
    first character in lowercase, otherwise, we add the character with an upper case. 
    return: 
    return new_str

tests = """
test_string = "hello" # Hello

flip_case(test_string)  # HEllO
assert flip_case(test_string) == test_string
# pass

test_string = "python" # Python

flip_case(test_string)  # pThOn
assert flip_case(test_string) == test_string
# pass

test_string = "allet" # ALLET

flip_case(test_string)  # AlE
assert flip_case(test_string) == test_string
# pass

test_string = "LOL" # LOO

flip_case(test_string)  # LOO
assert flip_case(test_string) == test_string
# pass

"""
```