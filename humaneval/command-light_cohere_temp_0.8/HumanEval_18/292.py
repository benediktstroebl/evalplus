```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    : overlapping matches allowed
   
    """
    # split the string
    words = string.split()
   
    words
    # remove the substring from all words
    new_words = [word for word in words if word not in words[words.index(substring)]
    words = [word for word in words if word.startswith(substring)]
    words = [word for word in words if word.endswith(substring)]
    words = [word for word in words if substring in word]
    """
    return sum(1 for _ in words)

# test the function
print(how_many_times('aaa', 'a')) # 3
print(how_many_times('aaaa', 'aa')) # 3
print(how_many_times('abcdeefabcba', 'abc')) # 6
```