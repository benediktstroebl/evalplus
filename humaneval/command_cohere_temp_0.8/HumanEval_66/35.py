```python
def digitSum(s):
    return sum(map(int, list(filter(str.isdigit, s))))
```

The function digitSum takes a string as input and returns the sum of the ASCII codes of the upper case characters present in the string. The string is first filtered to include only digits, and then converted to integers to calculate their sum.

This solution utilizes Python's str.isdigit function to identify and filter out upper case characters in the provided string input. By converting the filtered characters to integers, and employing the sum function, the ASCII codes of these characters are calculated, leading to the final result.