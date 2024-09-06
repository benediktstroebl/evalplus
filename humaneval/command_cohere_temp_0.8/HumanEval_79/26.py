Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes. Enjoy the code and please let me know if you'd like to have any explanations of how the logic works:
```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]     # Convert decimal to binary and remove '0b'
    return 'db' + bin_str + 'db'    # Add 'db' at the beginning and end for formatting

# Test Cases
assert decimal_to_binary(15) == 'db1111db'
assert decimal_to_binary(32) == 'db100000db'
```
You can add more test cases to ensure the function behaves as expected with different inputs. I added two test cases in this version of the code to cover the examples mentioned in the problem description.