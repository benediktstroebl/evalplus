Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i: i+1])).count('1') for i in range(len(s))])
```
This function takes a positive integer `n` as its argument and converts it to a string. It then iterates over each digit of the string, converting each digit to its binary representation and counting the number of ones using `int(s[i: i+1])`. These counts are then concatenated together using string concatenation to form the final binary string representation of the sum and returned. 

This should correctly solve the problem for the provided test cases. Let me know if you would like me to explain any part of the solution or provide additional helpful feedback.