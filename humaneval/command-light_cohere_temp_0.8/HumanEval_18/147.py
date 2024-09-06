```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This Python function, `how_many_times`, takes two parameters: a string and a substring. It uses the find() method from the substring in the string and returns the length of the match.

This function uses the `find()` function, which returns an integer `match` index if the `substring` is found in the string, and `None` otherwise. The `len()` function then uses the returned `match` index to get the length of the match.

This function is designed to efficiently solve the problem of counting the number of occurrences of a given substring in a given string.

You can use this function to solve this type of problems in your Markdown code.