```python
def is_happy(s):
    """
    Check if a string is happy or not.
    Returns True if the is happy and False otherwise.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    """
    length = len(s)
    if length < 3:
        return False
    s = s[::-1]  # Reverse string to get rid of the last 3 consecutive distinct characters
    for i in range(0, length - 3):
        if s[i] != s[i + 3]:
            return False
    return True
# Example usage
print(is_happy("abcdxyyx")))  # Output: True
print(is_happy("abc"))  # Output: False
``` 
The function checks if the length of the string is at least 3 and if every 3 consecutive distinct characters are the same. The function then reverses the string to ensure that the last 3 distinct characters are removed, and then it checks if the characters are distinct by iterating over the string and comparing the characters at positions i and i + 3.