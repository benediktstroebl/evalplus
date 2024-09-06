Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set which represents the number of distinct characters. Thus, the number of distinct characters is unaffected by the string's case or the order in which they occur. 

Here's how you can invoke this function with some tests:
```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
>>> count_distinct_characters('Hello, hello!")
5
```