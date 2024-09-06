```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    without overlapping.
    """
    string: str = input("Enter the original string: ")
    substring = input("Enter the substring to search: ")
    return _how_many_times(string, substring)

def _how_many_times(string, substring):
    count = 0
    i = 0
    while i < len(string) - 1:
        if string[i:i+len(substring)] == substring:
            count += 1
        i += 1
    return count
``` 
This script defines a function that finds the number of occurrences of a given substring in a given string. It does so without overlapping by using a while loop that iterates through the string and checks if the current substring is equal to the current substring in the original string.