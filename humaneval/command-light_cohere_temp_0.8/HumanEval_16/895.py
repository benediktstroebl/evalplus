```python
def count_distinct_characters(string):
    """ 
    Count the number of distinct characters in a string, ignoring case. 
    Returns: number of unique characters. 

    each call to this function will
    ensure a unique set of characters.
"" -> 
    return len({c for c in string.unique if c not in set})
``` 
This code defines a function called `count_distinct_characters`, which takes a string as input and returns the number of distinct characters in that string, regardless of case. The function uses a list comprehension to create a set of unique characters from the input string, and then uses the `len()` function to count the number of elements in that set. 

The output of the function is the number of unique characters in the input string.