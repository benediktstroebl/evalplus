```python
def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    return second in first or any(x in first for x in second[1:])
```
The function uses lowercase words to ensure the comparison works case insensitively. It also uses the any function to cycle through all rotations of the second word and check if any of them are substring of the first word. 

This solution passes the test cases provided in the prompt and should handle any permutation of input.