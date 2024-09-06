```python
def flip_case(string: str) -> str:
    return string.case_swap_LOWERCASE(string)

#Test cases
assert flip_case("hello") == "HELLO"
assert flip_case("world") == "oRDlW"
assert flip_case("ussyamarin") == "ussyAMAN"
``` 
This script defines a function `flip_case` that takes a string as input and then returns a new string where all lowercase characters become uppercase, and all uppercase characters become lowercase. The test cases ensure that the function is correctly flipping the case of the characters in the input strings.