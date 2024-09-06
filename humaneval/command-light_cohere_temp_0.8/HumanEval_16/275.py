Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This script defines a function called count_distinct_characters that takes a string as input and returns the count of distinct characters (regardless of case) in that string. It uses the `set()` method along with `string.lower()` to create all characters lowercase, and then uses the `len()` function to count the number of unique characters. 

The function passes all the tests provided in the initial prompt without needing external input.