```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The function digitSum leverages the sum function's ability to calculate the sum of elements in a collection by applying a lambda function that filters out only upper-case characters from the input string s and uses the ord() function to retrieve the ASCII value of each character. The resulting sum of these ASCII values equals the sum of the upper characters' ASCII codes in the input string s. This solution adheres to the problem statement by returning the targeted sum.