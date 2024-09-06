```python
def count_distinct_characters(string):
    """ 
    Count the number of distinct characters in a given string, 
    regardless of case. 
    Returns: number of characters in lowercase, uppercase, and digits. 

    This count = len(set(char for char in string if char.isalpha())) 
    """ Returns this count as the number of distinct characters. 
    """ 
    return count

string = "xyzXYZ"
print(count_distinct_characters(string))

```