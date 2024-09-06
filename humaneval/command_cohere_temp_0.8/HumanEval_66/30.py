```python
def digitSum(string):
    return sum(map(int, list(string.upper())))
```
This function uses the sum function to add up the results of mapping the int function to each character in the string. The map function applies the int function to each character in the string, and the list function ensures that the resulting characters are treated as numbers. Note that this approach ignores non-alphabetical characters.