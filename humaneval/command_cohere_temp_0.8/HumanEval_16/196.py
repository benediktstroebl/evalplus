Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store and count the distinct characters in the string regardless of case. The tests provided in the problem statement can be tested with:
```python
>> count_distinct_characters('xyzXYZ')
3
>> count_distinct_characters('Jerry')
4
```
This approach takes advantage of the set data structure in Python which automatically does not repeat values and is case-insensitive.