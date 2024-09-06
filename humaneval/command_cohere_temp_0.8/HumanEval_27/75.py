```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.islower() else char.swapcase() for char in string)
```

This script defines a function `flip_case` that takes a string as an argument and flips the case of its characters. It returns a string where all lowercase characters are converted to uppercase and all uppercase characters are converted to lowercase. This function achieves this by using a generator expression that iterates through each character in the input string. For each character, it checks if the character is in lowercase using the `islower()` method. If it is, it swaps its case using the `swapcase()` method, which converts it to uppercase. If the character is not in lowercase, it also uses the `swapcase()` method, but in this case, it converts the character to lowercase. The joined string is then returned as the result. 

The example usage provided in the problem statement would generate the following output when using this function:
```bash
'hELLO'
``` 

This approach uses Python's string methods for case manipulation and maintains good readability and efficiency. It avoids the need for a loop and provides a clear interpretation of the string manipulation. 
**NOTE**: This solution assumes ASCII characters for the purpose of swapping cases. With non-ASCII characters, this method would preserve the character's visual appearance but could affect the actual character encoding. Moral of the Story: Always consider character encoding when manipulating text!