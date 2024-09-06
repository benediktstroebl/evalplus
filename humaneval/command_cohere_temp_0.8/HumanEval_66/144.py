```python
def digitSum(string):
    return sum(ord(char) for char in string if char.isupper())
```
The function digitSum takes a string as input and returns the sum of the ASCII codes of the upper characters only. The ord() function returns the ASCII code of a character, and the sum() function returns the total of the ASCII codes. The isupper() function checks if the character is an uppercase letter. You can verify the correctness of the script with the provided test cases. Here is an example:
```python
print(digitSum("abAB")) # 131
print(digitSum("abcCd")) # 67
print(digitSum("helloE")) # 69
print(digitSum("woArBld")) # 131
print(digitSum("aAaaaXa")) # 153
``` 
This will output the following:
```
131
67
69
131
153
``` 
This demonstrates the expected functionality of the script, calculating the sum of the ASCII codes of the upper characters only in the provided strings. Feel free to test it with other strings as well. 
If you have any further questions or need additional assistance, please let me know! I'm here to help you understand this concept and assist with any other coding challenges you may face. Lifting your coding skills and making them shine!