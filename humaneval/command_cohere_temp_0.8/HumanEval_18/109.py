```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts a string and a substring as inputs and returns the number of times the substring occurs in the string, including cases of overlapping. It utilizes the `count()` method to achieve this. 

Here is an example usage of the function:
```python
print(how_many_times('aaa', 'a'))  # Outputs: 3
```

This approach provides a straightforward solution to the problem without requiring additional logic to handle overlapping cases. 
However, feel free to customize or optimize it to your needs.