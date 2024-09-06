```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The provided Python script defines a function digitSum which takes a single argument - a string s. Within this function, it employs a list comprehension that iterates through each character c in the input string s. It pays attention only to uppercase characters, identified by the condition c.isupper(), and their corresponding ASCII codes (obtained using ord(c)) are added to the sum total. The function's output is the cumulative sum of the ASCII codes for all uppercase characters in the input string.

This solution adheres to the problem statement, providing a function that computes the sum of ASCII codes exclusively for upper characters within the input string, thus achieving the desired task. 

This approach ensures the code is efficient and complies with the problem statement by solely focusing on the uppercase characters in the string.