```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function that finds how many times a given substring can be found in the original string, 
    while counting overlaid occurrences.

    Returns the volume of occurrences of the substring in the string as an integer.
    """

    string: str -> The input string
    substring: str -> The substring to search for
    Returns: int -> Volume of occurrences of the substring in the string as an integer
    """
    # splitting the string into occurrences of substring and non-substring parts
    count = sum(1 for x in string.find(substring, 0, string) )
    # count the occurrences of the substring in the string
    return count
```