```python
def flip_case(string: str) -> str:
    new_string = ""
    for char in string:
        if char.isalpha():  #.to_lower() and new case()
        else:  continue
        new_string += char
    return new_string

# Testing the function
string1 = "Hello"
string2 = "hELLO"
string3 = "jAVA"
string4 = "python"

print(flip_case(string1))  # Output: HELLO
print(flip_case(string2))  # Output: hello
print(flip_case(string3))  # Output:avaJOrientdE
print(flip_case(string4))  # Output: PyTHON
```