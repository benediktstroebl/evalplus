```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string. 
    Count overlapping cases.
    
    :param string: str The input string 
    :param substring: str the substring to search for 
    :return: int number of times the substring appears in the string
    """
    count = 0
    string = string.split()
    stringsub
    size of the substring and string 
    for i in range(1, len(string)):
        string[i] = string[i].lower() 
        if string[i] == substring:
            count += 1 
    return count

# Test the function
a = "aaa"
b = "hello"
c = "world!"
print(how_many_times(a,b))
print(how_many_times(a,c))
print(how_many_times(b,c))
print(how_many_times("Hello", "o"))
print(how_many_times("Hello", "ell"))
print(how_many_times("Bar", "Bar"))
``` 
The code defines a function called `how_many_times` that takes two arguments: a string and a substring. It then iterates over each string, and for each occurrence of the substring, it increments a count. 

The function then returns the number of times the substring appears in the original string.