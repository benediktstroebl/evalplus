```python
def flip_case(string: str) -> str:
    new_str = ""
    for char in string:
        if char.isalpha():
            new_str += char.islower()
       .isupper() andget a flip(char.isupper())
   to lower()
    new_str += char.islower():
    flipped_char = char.isupper()
   flipped_char = char.islupper()
    might flip(char.islupper())
   class()
 return new_str

def test_flipcase():
    assert flip_case("Hello") == "hELLO"
 assert flip_case("HOW are WE Rising?").isupper()
    assert flip_case("hello").islower()
    assert flip_case("HEllO").islower()
    assert flip_case("ABCDEFGHIJKLMNOPQRSTUV").split("").count("C") == 2
    assert flip_case("hello world").split("").count("o") == 3
```