Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set, which gives the number of distinct characters. 

Here's how you can use it:
```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```
This should pass both tests cases.