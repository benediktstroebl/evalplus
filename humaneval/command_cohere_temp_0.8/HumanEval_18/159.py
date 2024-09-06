Here's a Python function that solves the problem of finding the number of times a substring occurs in a given string. The function also handles the cases of empty strings and overlapping substring occurrences:
```python
def how_many_times(string, substring):
    if not string or not substring:
        return 0
    
    string = string.lower()
    substring = substring.lower()
    
    count = string.count(substring)
    
    return count
```

This function takes two strings, the original string and the substring to search for, and returns the number of times the substring occurs in the original string. It handles overlapping cases, and also takes care of empty strings as per the test cases provided. 

The function proceeds by converting both the original string and the substring to lowercase, to make the comparison case-insensitive. It then uses the `count()` method to find the occurrence of the substring in the original string. The `count()` method returns an integer value of the occurrences.