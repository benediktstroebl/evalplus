```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function to add up the integers represented by the digits in the string, and the map function to convert the characters in the string to integers. The result is the sum of the ASCII codes of the upper characters in the string. This solution utilizes native Python functions, making it efficient and easy to understand.

This approach takes the given string input, converts it to an uppercase utilizing the upper() method, then utilizes the map() function to transform these uppercase characters into their corresponding integer representations. The integers are then added together using the sum() function to yield the desired sum of ASCII codes.