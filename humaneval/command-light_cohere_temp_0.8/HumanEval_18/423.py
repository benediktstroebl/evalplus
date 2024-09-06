Here is a self-contained Python script with a function that solves the problem of counting the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string.
    """

    string = string.split()
    how many lines
    separated by newline 
    res = 0
    for i,line in enumerate(string):
        if(line == substring):
            res += 1
    return res

# test the function
print(how_many_times('aaa', 'aa'))
``` 
This script defines a function `how_many_times` that takes a string and a substring as input. It then splits the The lines of the string and uses a loop to count the number of occurrences of the substring within the original string. The function returns the count.