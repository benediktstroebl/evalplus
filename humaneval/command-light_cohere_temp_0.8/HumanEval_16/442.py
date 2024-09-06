Here is a self-contained Python function that finds the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    return len(set(string.lower()))
```
This function, count_distinct_characters, takes a string as input and uses the `set()` function along with `lower()` method to create a set of lowercase characters in the input string. 
The `len()` function is then used to calculate the length of this set, which is the number of distinct characters in the string.