```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the string, regardless of case.
    return: 
    """
    if not string:
        return 0
    lower_cased = string.lower()
    common_chars = set(lower_cased)
    return len(common_chars)

# Sample Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('jerry'))    # Output: 4
print(count_distinct_characters('zX'))        # Output: 3
``` 
This script defines a function `count_distinct_characters` which takes a string as input and returns the count of distinct characters in the string, regardless of case. It handles empty strings by returning 0, converts the input string into lowercase, and then creates a set of all lowercase characters in the string. It then uses the option of sets to find the distinct characters and finally, returns the length of this set.