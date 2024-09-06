Here's a Python script that contains a function to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    string = string.lower() 
    distinct_characters = set(string)
    return len(distinct_characters)
```
This function uses the `set` method to remove duplicate characters and ultimately count them. 

You can use the `lower()` function to make the string lowercase before counting the characters, thus ensuring that 'x' and 'X' are counted as the same character. This function passes the tests corresponding to the provided problem statement. You can test it with the following:
```python
>> count_distinct_characters('xyzXYZ')
3
>> count_distinct_characters('Jerry')
4
```
If you want to customize the script to handle uppercase letters differently, please let me know and I'll provide you with an alternative version.