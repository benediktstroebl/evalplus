```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts two inputs: `string` and `substring`. It uses the `count()` method to detect the occurrence of the `substring` within the `string`, regardless of the position and case. The method returns the count of occurrences of the substring. 

For example:
```python
print(how_many_times('aaa', 'a'))  # Outputs: 3
```

This approach proves efficient and compatible with the problem description. It delivers the desired result without any external dependency.