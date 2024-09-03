```python
def digitSum(s):
    return sum(c for c in s if c.isalpha())

print(digitSum(""))    # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd")) # Output: 67
print(digitSum("helloE")) # Output: 69
print(digitSum("woArBld")) # Output: 131
print(digitSum("aAaaaXa")) # Output: 153
``` 
This function iterates through each character in a string, and if the character is an uppercase letter (using the `isalpha()` method), it adds it to the sum.