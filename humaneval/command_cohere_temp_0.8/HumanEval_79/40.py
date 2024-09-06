Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes. 

```python
def decimal_to_binary(decimal):
    bin_string = bin(decimal)[2:]    
    return 'db' + bin_string + 'db'

# Test Cases
decimal_numbers = [15, 32]
expected_results = ['db1111db', 'db100000db']

for dec, result in zip(decimal_numbers, expected_results):
    assert decimal_to_binary(dec) == result
```

You can test this function with different input values to ensure it behaves as expected. Let me know if you would like to add more test cases or clarify any part of the code.