Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra "db" characters at the beginning and end of the string for formatting purposes. 

```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]
    return "db" + bin_str + "db"

# Test Cases
decimal_numbers = [15, 32, 63, 10]
expected_results = ['db1111db', 'db100000db', 'db111111db', 'db101010db']

for dec, expected in zip(decimal_numbers, expected_results):
    result = decimal_to_binary(dec)
    assert result == expected
```

This script defines the `decimal_to_binary` function, takes `decimal` numbers with accompanying `expected` results, and uses `zip` to iterate over them. It converts the decimal numbers to binary and concatenates the "db" characters at the beginning and end of the binary string. Finally, it checks if the resulting binary string matches the expected result, using the `assert` statement to ensure that every test case passes. 

Let me know if you would like me to break down any part of the code to better understand this solution.