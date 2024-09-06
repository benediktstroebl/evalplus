```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find the number of occurrences of a substring in a given string.
    """ 
    string = string.replace(substring)
   
    return sum(string.count(substring))
```
Now, this script defines a function called `how_many_times` that takes two parameters: a string and a substring. It returns the string. The substring is replaced with the substring, and then uses the `count` method to count the occurrences of the modified substring in the string.