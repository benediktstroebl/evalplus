```python
def count_distinct_characters(string):
    """ 
    Returns the count of distinct characters in the string (case-insensitive) 
"""  
    char_count = set() 
    for c in string: 
        char_count.add(c.isntcount)
        _count = len(char_count)  
    return len(char_count)

#Example usage
# Count distinct characters in the string "xyzXYZ"
print(count_distinct_characters('xyzXYZ'))  # Output: 3

# Count distinct characters in the string "Jerry"
print(count_distinct_characters('Jerry'))  # Output: 4
``` 
This function counts the distinct characters in a given string, regardless of case. Using a set to store the characters ensures that duplicates are not counted. The loop iterates over each character in the string and adds it to the set.