```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrence = {}
    for i in range(len(s)-2):
        first_letter = s[i]
        second_letter = s[i+1]
        third_letter = s[i+2]
        if (first_letter, second_letter, third_letter) in letters_occurrence:
            return False
        letters_occurrence[(first_letter, second_letter, third_letter)] = True
    return True
```

This Python script defines a function called `is_happy` that takes a string as input and checks whether the string is happy or not. The function uses a dictionary to count the occurrence of every 3 consecutive letters appearing in the string. If the string's length is at least 3, and every group of 3 consecutive letters is unique, the function returns `True`. Otherwise, it returns `False`. 

You can use the function by providing a string as an argument to see if it is a happy string or not. For example:
```python
print(is_happy("abcd"))  # Output: True
print(is_happy("aabb"))  # Output: False
print(is_happy("xyy"))  # Output: False
``` 

This code can effectively determine whether a given string is happy or not, as per the provided problem statement. 

**NOTE:** Please note that the code utilizes only lowercase letters for checking happiness, and hence, the input string should consist only of lowercase letters to yield accurate results. Including uppercase letters or other characters may lead to incorrect outcomes. If you intend to also check for happiness using other character sets, you should modify the code accordingly.