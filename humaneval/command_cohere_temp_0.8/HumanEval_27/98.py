```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert alphabetic characters to their flip case counterparts, while leaving non-alphabetic characters unchanged. It leverages Python's str.swapcase() method to reverse the case of alphabetic characters. The join() function is then used to combine the modified characters back into a single string.

To execute this code simply run the `flip_case` function with a string input like so:
```python
print(flip_case('Hello'))  # Outputs: hELLO
``` 

This will neatly flip the case of alphabetic characters while keeping non-alphabetic characters intact, achieving the desired effect of flipping the case of the given string.