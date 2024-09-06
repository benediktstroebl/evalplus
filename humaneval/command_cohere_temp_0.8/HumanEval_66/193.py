```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function to add up the integers represented by the digits in the string, and the map function to convert the characters in the string to integers. The map function applies the int constructor to each character in the string, and the list function ensures that the result is treated as a list, which allows the subsequent sum operation to work as expected. This treatment is essential as the sum function in Python works only on iterables, meaning it expects multiple items (e.g., lists, tuples, and strings), and if a single item is provided (e.g., just a string), it will raise a TypeError. 

The function does not explicitly handle an empty input, therefore, it will return a TypeError if the input is empty - you could add `if not string:` to explicitly check for this case. 

This solution assumes that the input string contains only letters or digits, and therefore does not correctly handle other types of characters.