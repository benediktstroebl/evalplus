Here's a Python script that contains a function related to the task stated in the code block:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the unique characters in the provided string, disregarding any case. It then returns the length of this set, which is the number of distinct characters in the string. This approach ensures a quick and efficient computation without the need for additional libraries.