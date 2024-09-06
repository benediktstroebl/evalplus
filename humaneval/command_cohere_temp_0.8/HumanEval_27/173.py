```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
This script defines a function `flip_case` that takes a string as an argument and flips the case of each character. The `join` method is used to concatenate the flipped characters back into a string. 

To verify the functionality, you can run the test case provided earlier in the script:
```python
>>> flip_case('Hello')
'hELLO'
```

This will return 'hELLO', confirming that the function correctly flips the case of the characters.