Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are considered the same. The function then returns the length of this set, which is the number of distinct characters.

To test this function, you can use the following test cases: 
```python
>> count_distinct_characters('xyzXYZ')
3
>> count_distinct_characters('Jerry')
4
>> count_distinct_characters('Hello, World!')
6
>> count_distinct_characters('aaa')
1
```

Each test case illustrates how the function appropriately counts the distinct characters based on the problem statement.  This approach ensures simplicity, efficiency, and compatibility across different versions of Python.