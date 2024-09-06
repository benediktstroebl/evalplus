```python
def flip_case(string: str) -> str:
    new_string = ""
    for char in string:
        if char.isalpha():  #.' correctness 
           new_char = char.isupper() 
        else: 
            new_char = char.tolower() 
        new_string += new_char 
    return new_string
```