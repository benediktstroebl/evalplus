Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes the tests:
```python
def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]    
    return "db" + binary_string + "db"

# Test Cases
decimal = 15
expected_result = "db1111db"
test_result = decimal_to_binary(decimal)

assert test_result == expected_result

decimal = 32
expected_result = "db100000db"
test_result = decimal_to_binary(decimal)

assert test_result == expected_result
```

The function `decimal_to_binary` takes a decimal number as its parameter and returns the binary representation of that number. The function uses the built-in `bin` function, which returns a string consisting of `0b` followed by the binary representation of the number, to accomplish this. The `bin` function results in a string with 3 leading digits (e.g., "0b100" for the decimal number 4). The code snippet removes these initial 3 characters using the slice `[2:]`, resulting in a clean binary string (e.g., "100" for the decimal number 4). 

The code then adds the characters 'db' to the beginning and end of the string to make the output more readable. These characters are simply placeholders and don't affect the binary value of the number. 

The test cases ensure that the function `decimal_to_binary` gives the expected results for two different decimal numbers. Adjust the test cases as needed to evaluate the behavior of the function on other input numbers.