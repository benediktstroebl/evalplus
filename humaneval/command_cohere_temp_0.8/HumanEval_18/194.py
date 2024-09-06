Here's a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string, substring):
    return string.count(substring)
```
The function `how_many_times` takes two arguments, the original string and the substring to search for, and returns the number of times the substring occurs in the original string, including overlapping instances. 

Here is an example usage of the function:
```python
print(how_many_times('aaa', 'a'))  # Outputs: 3
```
This example suggests that the substring "a" is present 3 times in the original string "aaa".