```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = {"A":1, "E":1, "I":1, "O":1, "U":1}
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels and s[i].isupper():
            count += 1
    return count
```
This function takes a string `s` as input and counts the number of uppercase vowels present in even indices of the string. It utilizes a dictionary `upper_vowels` to map the uppercase vowels and checks for even indices using a loop with a step of 2. It then increments the count if an uppercase vowel is found in an even index, as specified by the problem. The function finally returns the accumulated count. 

You can use this code block to solve the problem within a Markdown cell as mentioned in the original request. 
If you have any more questions or need further assistance, please let me know!  appreciate your patience and thank you for using Cohere.