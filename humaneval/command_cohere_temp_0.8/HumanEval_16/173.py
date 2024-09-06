Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store and count the distinct characters, ignoring case. The tests provided in the problem prompt can be simulated as:
```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
``` 
The code passes the specified tests and provides the required function to solve the problem.