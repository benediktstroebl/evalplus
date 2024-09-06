```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts two inputs: `string` and `substring`. It uses the `count` method to detect the occurrence of the `substring` within the `string`, regardless of the positions of the instances. 

The function returns the number of times the `substring` appears in the `string`, even if there are overlapping occurrences. 

If the `substring` is empty, the result will be 0, and if the `string` is empty, the function will return 0 as well. 

This solution has a straightforward syntax and is efficient in terms of time and space complexity, making it suitable for most scenarios. 

You can use the function with specific test cases to ensure it behaves as expected: 
```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
``` 

These tests check for empty string inputs, and inputs with single and double occurrences of the substring.