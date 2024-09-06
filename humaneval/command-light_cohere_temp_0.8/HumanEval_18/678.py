```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function that counts how many times a substring can be found in the original string, considering overlapping matches. 
    Parameters: 
    string: str, substring: str 
        Both are string inputs and must adhere to the string.string convention. 
    
    Returns string: A substring is being searched for in the original string. 
    Returns: number of occurrences of the substring in the original string. 
    """
    number = 0 
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            number += 1 
    return number

#Test cases
string1 = "aaaaaaa"
string2 = "aaaaaa"
string3 = "aaaaaaa"a"
string4 = "aaa"
substring1 = "aa"
print(how_many_times(string1, substring1)) 
print(how_many_times(string2, substring1)) ) 
print(how_many_times(string3, substring1)) 
print(how_many_times(string4, substring1)) 

``` 
This function, `how_many_times`, utilizes a loop to iterate over the characters of the original string and compares each character with the substring. It returns the  the number of times the substring appears in the string, accounting for case and character variations.