```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string.
    Count overlapping cases.
    """ Function times every possible string or basic string, just returns 0
    """
    if not substring:
        return 0
    return sum(1 for x in string.find(substring, x) > 0)

# Test the function
print(how_many_times('aaa', 'a')) 
print(how_many_times('aaaa', 'aa')) 

``` 
This code defines a function how_many_times that takes two parameters: a string and a substring. The function then checks if the substring is empty, and if so, returns 0. Then, the function uses a generator expression to iterate over the find method of the string with the substring. The function then checks if each match is greater than 0, and if so, adds 1 to the result.