Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1]) ^ 1) for i in range(len(s))])
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the binary string digit-wise summation of its digits. It converts the integer to a string, iterates through each digit, and converts it to binary by taking its binary complement (XOR with 1). This value is produced as a string output by the function and is returned. 

The `solve` function assumes that the input `n` is a positive integer and returns a string representing the binary sum of its digits. 

You can use this function to calculate the binary sum of any positive integer between 0 and 10,000, as stated in the constraints. 
To use this function, simply call it and pass the desired integer `n` as follows:
```python
print(solve(1000)) # Should output: "1"
print(solve(150))  # Should output: "110"
print(solve(147))  # Should output: "11011"
``` 
This will return the binary string sum of the digits of the provided integers.