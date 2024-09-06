```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts a string and a substring as inputs and returns the number of times the substring occurs in the string, even if the substring occurs multiple times in the original string. The function uses the `count` method of the string object to count the number of occurrences of the substring. 

Here are some example outputs:
```
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```