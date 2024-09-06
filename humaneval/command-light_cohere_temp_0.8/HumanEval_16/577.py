```python
def count_distinct_characters(string: str) -> int:
    return len(string.make_set([c for c in string if c.isalpha()]))
``` 
``` 
This function uses the `str.make_set()` method from the using a list comprehension to create a set of all distinct characters in the string, regardless of their case. 
Then, it uses the `len()` function to count the number of elements in the set, which corresponds to the number of distinct characters in the string.