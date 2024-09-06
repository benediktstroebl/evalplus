```python
def flip_case(string: str) -> str:
    return ''.join_(c.lower() if c.isalpha() case
   outines with input for the string, and the is now treated as an all-casing word. 
``` 
This function uses the `isupper` function to check if the character at index 0 of the string is an uppercase letter. If it is, the character is converted to lowercase. Otherwise, the character is converted to uppercase. 

It uses the `lower` function to flip the case of a character. 

Here is a test to see if the function is working correctly:
```python
def test_flip_case():
    return 'Hello'.flip_case() == 'hELLO'
test_flip_case()
```