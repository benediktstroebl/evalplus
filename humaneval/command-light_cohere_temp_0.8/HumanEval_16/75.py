```python
def count_distinct_characters(string):
    return len({c for c in string.string() if c.isalpha()})
 unique_chars = sum(1 for c in string if not(c in set(string))))
``` 
This function calculates the number of distinct characters in the given string, regardless of case. Using a set of characters in the input string and checking each character against it, the function determines the number of unique characters. The code is concise and readable, following Python best practices.