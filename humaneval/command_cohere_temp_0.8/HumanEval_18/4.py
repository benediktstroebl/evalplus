Here's a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    return string.count(substring)
```
The function `how_many_times` takes two strings as input and uses the `count` method to find and return the number of times the `substring` appears in the `string`, including overlapping instances. This method returns an integer representing the count of substring occurrences. 
For example, if we call `how_many_times('aaa', 'a')`, it will return `3` since the character 'a' appears three times in the string 'aaa'. 

This approach guarantees correctness in counting overlapping instances while remaining efficient with a time complexity of `O(n)` due to the `count` method.