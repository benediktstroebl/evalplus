Here is a self-contained Python script that defines a function to solve the problem you have described:
```python
def how_many_times(string, substring): 
    """ Count how many times a given substring can be found in the original string, considering overlapping cases.

    Args: 
        - string (str): The original string 
        - substring (sub): The substring to find

    Returns: 
        - count: Number of occurrences of substring in string
    """
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        i += 1
    return count

# Test cases
string1 = "aaa"
substring1 = "a"
string2 = "aaaa"aa"
string3 = "aaaaa"
print(how_many_times(string1, substring1)) 
print(how_many_times(string2, substring1)) 
print(how_many_times(string3, substring1)) 

```

This code defines a function `how_many_times` that takes two parameters: a string and a substring. The function uses a looping algorithm to count the occurrences of the substring in the original string, and returns the number of occurrences. 

It uses a while loop that iterates over the original string and checks if the current character is equal to the substring. This will continue until the string is completely traversed.