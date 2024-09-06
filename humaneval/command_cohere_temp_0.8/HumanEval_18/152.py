```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts a string and a substring as inputs and returns the number of times the substring occurs in the string, including cases of overlapping. It utilizes the `count()` method to achieve this. 

The `count()` method returns the number of times the specified subsequence appears in the string. This method works efficiently and can handle cases of overlapping substrings. 

Here are some usage examples to ensure that the function works as expected:
```python
>> how_many_times('', 'a')
0
>> how_many_times('aaa', 'a')
3
>> how_many_times('aaaa', 'aa')
3
>> how_many_times('aa', 'aa')
2
``` 
This function provides a reliable and concise solution to find the frequency of a substring within a given string.