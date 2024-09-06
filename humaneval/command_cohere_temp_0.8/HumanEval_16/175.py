Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set, which gives the required number of distinct characters. 

The `>>> ` assertions you provided are enough to demonstrate the function's behavior for this particular problem. If needed, I can generate additional test cases to ensure correctness.