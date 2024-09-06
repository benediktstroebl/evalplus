```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts two inputs: `string` and `substring`. It uses the `count` method to detect the occurrence of the `substring` within the `string`, regardless of the positions of the instances. 

The function returns the count of the substring in the given string. It assumes that both string and substring are initialized with appropriate values. 

You can use the function as follows:
```python
print(how_many_times('aaa', 'a'))
```

This will output:
```
3
```

This approach does not require any additional import statements, making the function self-contained within a Python environment.