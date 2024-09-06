Here's a Python script that contains a function to solve the problem as described in the code block:
```python
def count_upper(s):
    upper_vowels = "AEIOU"
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count
```

This function `count_upper()` takes a string `s` as input and counts the number of uppercase vowels in even indices. It utilizes a for loop to iterate through the string at even intervals, checks if the character is uppercase, and furthermore checks if it is a vowel using a separate string `upper_vowels` containing all the uppercase vowels. The count is incremented if these conditions are met. The function returns the final count of uppercase vowels in even indices. 

Here is an example of how you can use this function:
```python
print(count_upper("aBCdEf")) # 1
print(count_upper("abcdefg")) # 0
print(count_upper("dBBE")) # 0
```
The function's output should be as follows:
```
1
0
0
```
This is consistent with the problem's statement wherein the function counts the number of uppercase vowels in even indices of the string.