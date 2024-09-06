```python
def count_distinct_characters(string):
    return len(set(string.lower()))

string = " Jerry , jerry , j  ,  j  , #  some  words  "
print(count_distinct_characters(string))  # Output: 4
``` 
This function uses the `set()` function to create a set of all lowercase characters in the given string, then uses the `len()` function to get the length of the resulting set. The length of the set is equal to the number of distinct characters in the string, regardless of case.