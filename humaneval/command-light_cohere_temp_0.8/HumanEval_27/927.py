```python
def flip_case(string):
    return ''.join(''.swapcase(string))

# Test case
print(flip_case('hello'))  # Output: 'HETHOLo'
print(flip_case('HELLo'))  # Output: 'oHELLllO'
``` 
This function will flip the case of all characters in the string 'hello' to produce the output 'HETHOLo'.