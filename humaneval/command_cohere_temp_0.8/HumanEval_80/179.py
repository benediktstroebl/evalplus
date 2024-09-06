```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i+1], s[i+2]])) != 3:
            return False
    return True
```

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function first checks if the length of the string is equal to or greater than 3. If the length is less than 3, it returns `False` since happiness cannot be guaranteed with such a short string. Otherwise, it proceeds to iterate through the string, excluding the first and last characters. It checks if the set of consecutive letters with a gap of 3 between them is of size 3. If it is not, this means that there are repeated letters within this window, and the string is not happy, hence the function returns `False`. If the loop completes without encountering any repeated letters in the designated windows, the function returns `True`, indicating that the string is happy.

The script assumes valid input, i.e., a string or a list of strings.  It does not check for any validity of input beyond that. 

The script could be enhanced with more robust input validation and better handling of corner cases, although this would add more complexity and potentially overhead to the solution.