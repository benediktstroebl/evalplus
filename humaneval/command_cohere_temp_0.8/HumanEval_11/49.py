```python
def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```
The provided Python script solves the problem by translating both input strings `a` and `b` to binary numbers, performing an XOR operation on these numbers, translating the result back to a string, and returning it. This is done using the int() function to convert the strings to integers, the `^` operator to perform the XOR operation, and the `bin()` function to convert the number back to a binary string for the result. 

Here is an example usage of the function and the expected outcome:
```python
print(string_xor('010', '110')) # Expected Output: '100'
```
The function can be tested against other inputs to ensure it meets the requirements for the problem.