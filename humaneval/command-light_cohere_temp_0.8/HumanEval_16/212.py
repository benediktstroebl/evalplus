```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the given string (case-insensitive) """
    string = string.translate(str.maketrans(),
       
string = str.count(string.translate(str))
return len(set(string))
```