```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    return len(set(char for char in string.strip()))
``` 
# Example usage:
string = "xyzXYZ jerry JOSE"
result = count_distinct_characters(string)
print("Distinct characters:", result)
``` 
This function, when given a string, returns the count of distinct characters in it. Each distinct character is the character (in any case) is added to the set and counted.