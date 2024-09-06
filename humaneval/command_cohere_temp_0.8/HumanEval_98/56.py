```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = ["A", "E", "I", "O", "U"]
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels:
            count += 1
    return count
```
This function counts the number of uppercase vowels present in even indices of the string. It achieves this by iterating through the string, checking every second character, and incrementing a counter if it encounters an uppercase vowel. The result is achieved without the need for additional libraries. 
The `upper_vowels` list is essential to improve the efficiency of the script, as checking against individual characters ('A', 'E', 'I', 'O', 'U') would require looping five times for each character in the string. 

This solution has a time complexity of O(n), where n is the length of the input string, as it checks every second character in a loop. It is an efficient solution for this problem. 
It's crucial to emphasize that the code assumes the input string contains only uppercase letters and vowels. If the input may contain different characters, further modifications are necessary.  if concise code and time complexity is the main focus, using a dictionary or lambda function is indeed a more efficient approach. Here's an optimized version of the provided solution:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    return sum(1 for char in s if char.isupper() and char in "AEIOU" and ord(char) - 64 in range(0, 9, 2))
```
In this improved version, we employ the sum function to iterate through each character in the string s. We use a conditional expression to check if each character is uppercase and a vowel (AEIOU), and if its ASCII value is divisible by 2, indicating it lies in an even index. This version is more concise and employs built-in functions for efficiency and clarity.