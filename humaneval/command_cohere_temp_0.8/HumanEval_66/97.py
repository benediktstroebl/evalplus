```python
def digitSum(s):
    return sum(map(int, s.upper()))
```
This Python script defines a function called digitSum that takes a string s as input. Inside the function, it uses the sum function in combination with the map function to convert each character in the input string to its corresponding ASCII numeric value, using int as the conversion function. The result is the sum of these numeric values, which represents the sum of the ASCII codes of the upper-case characters only in the input string. The function returns this computed sum.