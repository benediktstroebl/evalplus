```python
def flip_case(string: str) -> str:
    new_string = ""
    for char in string:
        if char.isalpha():  #.to_upper()(char)
        else:
            new_string += char.isupper()
   
return new_string

# Test the function
test_flip_case = flip_case
test_flip_case("Hello")
test_flip_case("world")
test_flip_case("great")
test_flip_case("HeLLo RAllO"))
test_flip_case("!!!#")
test_flip_case("A"))
test_flip_case("Z")
test_flip_case("aa"))
test_flip_case("[][][])")
```