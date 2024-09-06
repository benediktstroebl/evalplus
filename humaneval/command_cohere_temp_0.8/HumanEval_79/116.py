Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return 'db' + binary + 'db'

# Test cases
decimal = 15
result = decimal_to_binary(decimal)
print(f"Test case: {decimal} in Decimal -> {result} in Binary")

decimal = 32
result = decimal_to_binary(decimal)
print(f"Test case: {decimal} in Decimal -> {result} in Binary")

decimal = -1
result = decimal_to_binary(decimal)
print(f"Test case: {decimal} in Decimal -> {result} in Binary")

decimal = 0
result = decimal_to_binary(decimal)
print(f"Test case: {decimal} in Decimal -> {result} in Binary")

decimal = 999
result = decimal_to_binary(decimal)
print(f"Test case: {decimal} in Decimal -> {result} in Binary")
```

In the code above, the `decimal_to_binary()` function takes a decimal number as its input. It converts this decimal number to a binary string using the `bin()` function, excluding the leading '0b'. It then returns the binary string with 'db' prefixes and suffixes to conform to the specified output format.

The test cases provided demonstrate how the function handles various decimal numbers, and the results are printed to the console. Note that the `print` statements can be adjusted according to your preferred output style.