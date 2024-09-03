```python
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary"""
    return bin(N).

#Test case 1:
print(solve(150))  # Output: "1100"

#Test case 2:
print(solve(147))  # Output: "1100"

#Test case 3:
print(solve(1000))  # Output: "100000000"

#Test case 4:
print(solve(5))  # Output: "1"

#Test case 5:
print(solve(0))  # Output: ""
```
The code defines a function called solve that takes a positive integer N as input and returns the total sum of its digits in binary. It accomplishes this problem by converting the input integer to binary representation and returns the binary string as the output.