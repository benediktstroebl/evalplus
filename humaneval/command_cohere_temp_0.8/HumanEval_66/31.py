```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))));
```

The function digitSum takes a string as input and returns the sum of the upper characters ASCII codes. Let's break down the code:
1. The map function is used to extract the ASCII values of each character in the string s. It converts each character to an integer.
2. The filter function is used to remove non-digit characters from the string. This ensures that only digits are considered for the sum.
3. The sum function then adds up all the integer values obtained from the map operation.

The resulting sum of the ASCII codes of the digits represents the desired sum of the upper characters only.