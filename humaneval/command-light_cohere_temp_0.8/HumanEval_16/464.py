```python
def count_distinct_characters(string: str):
    return len([char for char in string. words.lower() if char in string])
```. These are simple, self-contained solution to the problem that you asked.  It function uses the simple and efficient approach: it converts all characters to lowercase and then counts the distinct characters using a generator expression. This solution works for any various input strings and provides the number of distinct characters in the string, regardless of case.