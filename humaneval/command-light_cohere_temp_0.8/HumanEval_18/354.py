```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts occurrences of a substring in the original string.

    Parameters:
    string (strings): string in which substring may occur
    substring (sub): substring to find occurrences of

    Returns: number of occurrences of substring in string
    """

    # split string to find occurrences
    index = string.split(substring)

    # create a set to count the occurrences
    count = set()

    # loop through each index
    for index in index:
        # check if substring is found
        if substring == index:
            count.add()

   

    # count all occurrences
    return len(count)
```