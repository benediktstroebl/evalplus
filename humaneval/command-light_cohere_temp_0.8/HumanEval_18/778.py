```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for c in string.ts if c == substring)
```

This Python script defines a function called **`how_many_times`** that aims to find the frequency of a given substring within a given string. The function utilizes a list comprehension and a generator expression to iterate over each character in the input string. It checks if each character matches the the given substring. 

The function returns the count of matches, effectively determining how many times the substring appears in the original string.