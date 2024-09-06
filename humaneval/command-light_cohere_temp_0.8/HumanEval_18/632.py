Here is a Python script that contains a self-contained function that solves the problem you described:
```python
def how_many_times(string, substring):
    """ 
    Count the number of occurrences of a given substring in the original string.
    """ 
    return len(string.find(substring, string))

# Example usage:
string = "aaaaaa"
substring = "a"
result = how_many_times(string, substring)
print(result) # Output: 3
```