Here is a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string, substring): 
    """ Count the number of occurrences of a substring in the original string. 
    Args: 
        string (str): input string 
        substring (str): substring to search 
    Returns: 
        int: number of occurrences of substring in string
   """
    return sum(1 for c in string.find(substring, 0, len(string)))

# Testing the function 
def test():
    string = "aaaaaaa"
    substring = "aa"
    result = how_many_times(string, substring)
    print("Number of times the substring is: " + str(result))

test()
```
The code defines a function how_many_times that takes two arguments: a string and a substring. The function uses the string. It returns an integer value that is the count of occurrences of the substring in the string, including overlapping occurrences.