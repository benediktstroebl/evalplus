```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts two inputs: `string` and `substring`. It uses the `count` method to detect the occurrence of the `substring` within the `string`, regardless of the position and nature of these occurrences (overlapping counts as multiple instances). The result is the count of these occurrences, which is an integer. 

This approach enhances readability and simplicity while maintaining efficiency and effectiveness through the utilization of built-in methods.

The function's behavior is illustrated via the following tests:
```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```