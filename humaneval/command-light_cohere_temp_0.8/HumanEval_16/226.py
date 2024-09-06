```python
def count_distinct_characters(string: str):
    return len(set(string.lower()))
```

Here is a detailed breakdown of the solution:
- The function `count_distinct_characters`  takes one argument: `string`, which is the input string to be processed.
- Inside the process, it converts the entire input string to lowercase using the `lower()` method. This is result is a lowercase string, and we can then easily create a set from it.
- The resulting set will only contain unique characters from the original string, regardless of their case, which means that duplicate characters will be counted just once.
- The set has a length of `len(set(...))`, which is the number of unique characters in the string.
- We then return this length as the number of distinct characters in the original string.

This function can be used to efficiently count the number of distinct characters in any given string, which can be useful in a variety of text processing tasks.