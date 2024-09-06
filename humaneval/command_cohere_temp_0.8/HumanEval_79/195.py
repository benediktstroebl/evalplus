Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes corresponding tests:
```python
def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    return "db" + binary_string + "db"

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result) 

```

In the code, we utilize the built-in `bin` function, which returns a binary representation of a number. The code skips the '0b' part of the representation and adds the extra 'db' characters as per the prompt's instructions. The example usage demonstrates how to use the function correctly.