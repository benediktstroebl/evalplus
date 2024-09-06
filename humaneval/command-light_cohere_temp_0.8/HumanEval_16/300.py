Here is a self-contained Python function that solves the problem you described: 

```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a given string, ignoring case.
    return: int
    """
    # convert all characters to lowercase to make the comparison case-insensitive
    string = string.join(''.lower()
    string
   
    # use set to find unique characters
    set1 = set(string)
    count = len(set1)
    return count
    """

This function first converts all characters to lowercase to make the comparison case-insensitive, then uses the `set` data structure to find the unique characters in the string, and finally counts the number of these unique characters. 

Note that this function does not require any external variables or data and can be self-contained within the provided function definition.