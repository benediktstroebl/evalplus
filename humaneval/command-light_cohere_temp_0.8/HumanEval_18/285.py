```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    """
    strings that do not contain the substring will return 0, as substring 'a' does not appear.

    """
    strings that contain duplicates of substring will return the number of unique occurrences + 1.
    return sum(1 for i,j if string.contains(substring) and substring in substring are the same)
```
This code defines a function that accepts two arguments: a string and a substring. It then returns an integer indicating the count of the number of occurrences of the substring in the string. This is using a method of the first letter of the substring to check if it exists in the string, and sums up the counts for all such occurrences to get the total count.