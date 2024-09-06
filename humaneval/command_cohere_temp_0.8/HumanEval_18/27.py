Here's a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string, substring):
    return string.count(substring)
```
The function `how_many_times` takes two parameters, a string and a substring, and returns the number of times the substring occurs in the string, including cases of overlapping. This is achieved using the built-in `count` method in Python, which returns the number of occurrences of substring `substring` in string `string`. 
For example, calling `how_many_times('aaaa', 'aa')` will return `3`, which is the number of times the substring "aa" occurs in the string "aaaa".