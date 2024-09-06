Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses the `set` function to remove duplicate characters, and the `len` function to count the number of distinct characters, regardless of case, making it true to the problem statement. You can verify that this function passes the tests provided in the original prompt:
```python
>> count_distinct_characters('xyzXYZ')
3
>> count_distinct_characters('Jerry')
4
``` 
This solution is concise and effective in handling the problem. It presents the character counting mechanism without extraneous complexity.