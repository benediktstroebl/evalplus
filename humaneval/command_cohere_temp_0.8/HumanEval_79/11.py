Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes. 

```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]    
    return 'db' + bin_str + 'db'
```

In this code block, the function `decimal_to_binary` takes a numeric parameter `decimal`. The function uses the `bin` function on the parameter `decimal`, slices the resulting binary string from the third character onwards using the slice notation `bin(decimal)[2:]`, and returns a string that prefaces and suffaces the binary string with 'db' characters. These extra characters are added to maintain a specific format for the binary string.  This code block, when executed, will appropriately convert a decimal number to its binary representation with the specified formatting.