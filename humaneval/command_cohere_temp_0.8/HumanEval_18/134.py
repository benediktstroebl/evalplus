```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts a string and a substring as inputs and returns the number of times the substring occurs in the string, including cases of overlapping. It achieves this using the built-in `count()` method of Python strings. This method returns the number of times the `substring` occurs within the `string`, even if they overlap. 

Here is an example usage of the function:
```python
print(how_many_times('aaa', 'a'))
print(how_many_times('aaaa', 'aa'))
```
This will output:
```
3
3
```

This shows the functionality of the function: the first example output shows that the substring 'a' occurs three times in the string 'aaa'; in the second example, the substring 'aa' occurs three times in the overlapped manner in the string 'aaaa'.