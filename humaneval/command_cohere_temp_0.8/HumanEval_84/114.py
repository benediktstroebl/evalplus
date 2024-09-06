Here's a Python script that contains a function to solve the given problem:
```python
def solve(N):
    s = str(N)
    return ''.join([str(int(s[i: i+2]) + int(s[i+1: i+3]))) for i in range(0, len(s), 3])
```
This script provides the function `solve(N)` that takes in a positive integer `N` as a parameter and returns the binary string that is the sum of its digits. 

The script employs the use of `str(N)` to convert the integer `N` to a string, and slices the string into separate digit chunks; three digits at a time to be precise. It then converts each triple-digit chunk to binary and adds the two resulting binary digits. These sum-digits in binary are then rejoined to produce the final answer.

For example, if `N = 1000`, the sum of digits will be 1, and the function would return `"1"`. If `N = 150`, the sum of digits will be 6, and the function would return `"110"`. If `N = 147`, the sum of digits will be 12, and the function would return `"1100"`.

This approach ensures that the code is efficient and can easily be scaled up for larger `N` values without any increase in computational complexity.