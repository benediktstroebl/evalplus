```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert all characters to the opposite case and leaves non-alphabetic characters unchanged. It joins the resulting characters back into a string and returns the flipped result. 

To execute the function, simply call it with a string argument, as demonstrated in the following example: 
```python
print(flip_case('Hello')) 
```

This will output: 
```
hELLO
``` 
As per the problem definition, the string "Hello" has been flipped and rearranged with alphanumeric characters in opposite cases.