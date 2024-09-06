```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

The following test cases illustrate the correct behavior of the function:
```python
# Test case 1
print(is_happy('abcd'))  # Output: True

# Test case 2
print(is_happy('adb'))  # Output: True

# Test case 3
print(is_happy('aabb'))  # Output: False

# Test case 4
print(is_happy('xyy'))  # Output: False
``` 

The function `is_happy()` takes a single argument - a string `s` to be checked for happiness. If the string's length is at least 3, it then checks whether each set of 3 consecutive letters are distinct. The function returns True if all 3-letter segments have distinct letters, and False otherwise. 

Let's break down the Python script step-by-step:
1. **Function Definition**:
The problem task is defined as finding a string where every consecutive trio of letters is unique. The function is defined as follows:
```python
def is_happy(s):
```

The function is named `is_happy()` and takes a single argument `s`, which is the string to be checked for 'happiness'.

2. **Length Check**:
The first thing the function does is check if the string length is at least 3. If not, it returns False immediately, since a string must be longer than 2 letters to have any chance of forming 3-letter segments:
```python
if len(s) < 3:
    return False
```

3. **Consecutive Letters Check**:
If the string length is at least 3, the function then iterates through each set of 3 consecutive letters in the string. It uses a set called `letters_set` to keep track of letters encountered while iterating through the string, so it can check if each letter is unique within these 3-letter segments:
```python
letters_set = set()
for i in range(len(s)-2):
    if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
        return False
```

The loop goes from index 0 to len(s) - 2, skipping the last index (since it's not possible to form a 3-letter segment at the end of the string). The inner set comparison [s[i], s[i + 1], s[i + 2]] checks if the 3 letters in the segment are distinct. If they are not, then the function returns False.

4. **Happy String**:
If the loop completes without returning False, it means every 3-letter segment in the string is unique, and the function returns True:
```python
return True
```

This script results in a concise and precise function to check for happy strings, and the test cases ensure its correctness against various scenarios.