Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return f"db{binary}db"
```
This method converts the decimal number to binary using the `bin` function, and then takes the 2nd segment (excluding '0b') and appends 'db' to the beginning and end to meet the specified format. It's important to note that while this approach is straightforward, it's not the most efficient method for large numbers as it relies on string concatenation.

To better suit the given test cases, we can add some additional checks to handle situations where the provided input isn't a valid integer:
```python
def decimal_to_binary(decimal):
    if not isinstance(decimal, int):
        raise ValueError("An integer is expected")
    
    binary = bin(decimal)[2:]
    return f"db{binary}db"
```
This modification raises a `ValueError` if the input is not an integer, providing a more robust approach that can handle a wider array of inputs.

Let me know if you'd like to discuss further optimizations or any other details!