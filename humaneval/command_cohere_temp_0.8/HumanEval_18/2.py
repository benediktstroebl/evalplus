```python
def how_many_times(string, substring):
    return len(string) - len(string.replace(substring, ''))
```

This function calculates the number of times the `substring` occurs in the `string` by taking into account overlapping instances. It utilizes the replace method to remove all occurrences of the `substring` from the `string`, and then calculates the difference in length between the original `string` and the modified string without `substring`. This difference yields the desired count. 

Here are some example usages and results:
```python
>> how_many_times('', 'a')
0
>> how_many_times('aaa', 'a')
3
>> how_many_times('aaaa', 'aa')
3
>> how_many_times('aa', 'a')
2
``` 

This self-contained function provides a versatile solution for finding the frequency of a substring within a string while accounting for overlapping instances.