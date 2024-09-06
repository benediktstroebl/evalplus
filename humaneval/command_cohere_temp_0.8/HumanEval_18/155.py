Here's a Python function that solves the problem you've described:
```python
def how_many_times(string, substring):
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count
```

This function takes two strings as input: the `string` and the `substring`. It counts the number of times the `substring` appears in the `string`, including cases of overlapping. It uses a loop to compare the `substring` to consecutive portions of the `string`, each of length equal to the length of the `substring`. The `count` variable is incremented each time a match is found. The function returns the total count of matches. 

The function handles edge cases appropriately, as tests show:
```python
""" Find how many times a given substring can be found in the original string. Count overlaping cases.
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
"""
>>> how_many_times('aaa', 'b')
0
``` 
The first test checks an empty string input and empty substring and returns 0. The next two tests check the function with non-empty strings and different substring sizes, and the last test checks the function with different strings and a non-existing substring, returning 0 in all cases.