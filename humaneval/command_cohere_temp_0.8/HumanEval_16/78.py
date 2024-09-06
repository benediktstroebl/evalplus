Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set which gives the number of distinct characters. The function ignores the case, ensuring that 'a' and 'A' are considered the same character. The tests provided yield correct results:
```python
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
``` 
This solution can be easily copied and pasted into a Markdown code block to provide a quick solution to the problem.