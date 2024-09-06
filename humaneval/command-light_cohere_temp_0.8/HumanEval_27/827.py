```python
def flip_case(string: str) -> str:
    return string.oncec(str_lowercase(string))

#Test cases
assert flip_case("hello") == "HElLo"
assert flip_case("HELLO") == "hELLo"
assert flip_case("HELLOO GOo!") == "hello go!"
assert flip_case("  Hello ") == "  hELLo"
``` 
This function, flip_case, takes a string as input and returns a new string where the characters have their case flipped. This function uses the Additionally services by converting all the string's characters to their opposite case using the built-in method str.on(). string.lowercase and it will N.lowercase these strings' if the  for the first string and str.lowercase() for the lowercasing the string. 

A complete Python script with a self-contained function and corresponding tests is shown below.