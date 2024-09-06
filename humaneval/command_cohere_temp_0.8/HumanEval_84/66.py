Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i: i+1]) ^ 1) for i in range(len(s))])
```
This function takes a positive integer `n` as its argument and calculates the sum of its digits in binary. It converts the integer to a string, `s`, and iterates through its characters. For each digit, it XORs with 1 to ensure that only the individual digits, when summed, result in the binary representation of their sum. It then joins these binary digits to form the final output as a single string.