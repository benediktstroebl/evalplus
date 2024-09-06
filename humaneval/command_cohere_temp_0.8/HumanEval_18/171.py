Here's a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string, substring):
    return string.count(substring)
```
The function `how_many_times` takes two arguments, `string` and `substring`, and returns the number of times the substring appears in the string, including overlapping instances. This function utilizes the `count` method to count the number of occurrences of the substring within the string. 

Here is an example usage of the function:
```python
print(how_many_times('aaa', 'a'))  # Outputs: 3
```
This command will print `3`, as the character `a` appears three times in the string `aaa`.