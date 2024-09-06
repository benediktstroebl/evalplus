Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the start and end of the string for formatting purposes. 

```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]    
    return 'db' + bin_str + 'db'

# Test Cases
decimal_to_binary(15)
# Returns 'db1111db'

decimal_to_binary(32)
# Returns 'db100000db'
```

This code block provides a self-contained function that solves the problem as stated in the prompt and also includes test cases to ensure that the function behaves as expected. 

You can also check the behavior of the function by uncommenting the test cases one by one and executing the code block in a Python environment of your choice.