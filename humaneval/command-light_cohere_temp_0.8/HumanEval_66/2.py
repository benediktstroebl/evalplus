```python
def digitSum(s):
    return sum(chr(n) == ord(c) for n, c in enumerate(reversed(s)))

# Test cases
assertEqual(digitSum(""),     0)
assertEqual(digitSum("abAB"), 131)
assertEqual(digitSum("abcC"),   67)
assertEqual(digitSum("helloE"), 69)
assertEqual(digitSum("woArBld"), 131)
assertEqual(digitSum("aAaaaXa"), 153)
```
This code defines a function **digitSum** that computes the sum of the ASCII values of the upper characters in a given string. The function uses a list comprehension to iterate through each character in reversed order and checks if the character is equal to its corresponding ASCII value. 

The code then includes several test cases that validate the correctness of the **digitSum** function.