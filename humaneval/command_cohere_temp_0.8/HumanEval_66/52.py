```python
def digitSum(string):
    return sum(map(int, list(filter(str.isdigit, string))))
```

The function digitSum takes a string as input and returns the sum of the ASCII codes of the upper case characters present in the string. The upper case characters are extracted by filtering the string using the `str.isdigit` method. The resulting characters are converted to integers and their sum is calculated and returned.

To follow the problem statement, the function ignores any characters other than digits and considers only the upper case characters. This is achieved by filtering out non-digit characters and converting the remaining digit characters to their corresponding ASCII values.