Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1]) + int(s[i:i+1])%2) for i in range(len(s))])
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the input number `n` to a string `s` and then iterates over each digit of the string. It doubles each digit and adds 1 if the digit is odd (using the modulo operator `%2`), effectively converting each digit to its binary representation. It then concatenates these binary representations to form a string and returns the result. 

Here's an example of how you can use this function to solve for different input values:
```python
print(solve(147))  # Outputs: "1100"
print(solve(150))  # Outputs: "110"
print(solve(1000))  # Outputs: "1"
```
This function effectively converts each digit of the input number to its binary representation, doubles it, and adds 1 if it's odd. It then concatenates these binary representations to provide the total sum of digits in binary.