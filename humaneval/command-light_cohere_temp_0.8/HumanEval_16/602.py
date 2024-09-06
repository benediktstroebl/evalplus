```python
def count_distinct_characters(string):
    """ Returns the count of distinct characters in the given string (case-insensitive) """
    string = string.upper()
   
   .lower()
    create a all a list of unique characters, then count the number of distinct ones.
    return len([char for char in set(string) if char.isalpha()]
print("Distinct characters:", len([char for char in set(string) if char.isalpha()]))
```