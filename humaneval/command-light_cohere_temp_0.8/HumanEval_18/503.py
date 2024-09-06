Here's the provided Python code:
```python
def how_many_times(string, substring):
    """ Count the number of occurrences of a substring in the original string, ignoring case and overlapping matches """
    return len([i for i,x in enumerate(string.find(substring)])
```
This code defines a function `how_many_times`, which takes two parameters: a string and a substring. The function uses the general purpose method `find` to iterate over each character in the string and count the occurrences of the substring, and returns the result.