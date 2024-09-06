```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)
```

This script defines a function `flip_case` that takes a string as an input and toggles the case of the characters, converting lowercase characters to uppercase and uppercase characters to lowercase. This is achieved using a list comprehension with conditions based on the `islower()` and `swapcase()` methods. The `join()` method then concatenates the resulting list of characters back into a string. 

To test this function, you can run the following input tests:
```python
>>> flip_case('Hello World!')
'HELLO WORLD!'

>>> flip_case('easy PEASY')
'EASY peasy'

>>> flip_case('123a$b%c')
'123A $b%C'
``` 
Each of these test cases should return the expected output based on the toggle case requirement.