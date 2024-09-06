```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.
    Example: 
    Return the minimum number of occurrences.
    """

    following steps:
    1. Remove all occurrences of the string except the substring using set() 
    2. Count the number of remaining characters in the string
    3. Count the number of occurrences of the substring
    4. Return the total count of occurrences.

# Test

# Test with different cases. 
string = "aaaaaa"
substring = "aa" 

count = how_many_times(string, substring)
print(count)  # Output: 3

string = "hello"
substring = "ello" 

count = how_many_times(string, substring)
print(count)  # Output: 1
```