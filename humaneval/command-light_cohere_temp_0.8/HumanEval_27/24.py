```python
def flip_case(string: str) -> str:
    new_str = ""
    for c in string:
        if c.isalpha():
            new_str += c.isuppersl():
            new_str += c
    else:
        new_str += c.isupper() and
    flip_case(new_str)
    return new_str

# Test cases
# Ensure all strings are valid
def test_flip_case():
    assert flip_case("Hello") == "hELLO"
    assert flip_case("WOW") == "owW"
    assert flip_case("INeeded Flip") == "eedINFliFX"
    assert flip_case("abc") == "Cbc"
    assert flip_case("A") == "a"
    assert flip_case("Z") == "z"
``` 
This script defines a function `flip_case` that converts a given string to a new string with characters swapped between lowercase and uppercase. It also provides several test cases to ensure the function's correctness.