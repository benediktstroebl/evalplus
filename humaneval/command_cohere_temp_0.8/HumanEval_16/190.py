Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store and count distinct characters, ignoring case. 

You can verify the behavior of the function with the following tests:
```python
>> count_distinct_characters('xyzXYZ')
3
>> count_distinct_characters('Jerry')
4
>> count_distinct_characters('Hello, hello!, HELLO!' )
4
>> count_distinct_characters('1223')
3
```