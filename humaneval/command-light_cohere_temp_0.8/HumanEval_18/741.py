```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, without overlapping.
    >>> string = 'aaaaaaa'
    sub = 'a'
    result = 0
    length_string = len(string)
    for i in range(length_string):
        if string[i:i+len(substring)] == sub:
            result = result + 1
    return result

# Test the function with various cases
string1 = 'aaaaaaa'
substring1 = 'a'
result1 = how_many_times(string1, substring1)
print("Result for " + string1 + " and " + substring1 + " is : " + result1)

string2 = 'abcba'
substring2 = 'a'
result2 = how_many_times(string2, substring2)
print("Result for " + string2 + " and " + substring2 + " is : " + result2)

# String with only substring present
string3 = 'aab'
substring3 = 'a'
result3 = how_many_times(string3, substring3)
print("Result for " + string3 + " and " + substring3 + " is : " + result3)
``` 
The above Python code defines a function `how_many_times` that counts how many times a given substring can be found in an original string.  The function accepts two parameters: a string and a substring. It uses a string matching algorithm without overlapping to calculate the result.