```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i+1])] > 1 or letters_count[ord(s[i+2])] > 1:
            return False
    return True
```

The algorithm works by first checking if the string's length is at least 3, which is the minimum required length for a happy string. If the string is shorter than 3 characters, it immediately returns `False`.

Next, we initialize a counter for each possible ASCII letter. The counter is initially set to 0 for each possible ASCII value (0-255) and will be used to track the frequency of each letter in the string.

Then, we iterate through the string and increment the appropriate counter for each letter.

After that, we again iterate over the string in steps of 3 letters. We check if any of the counters are greater than 1, indicating that the consecutive letters are repeated. If any of these conditions are met, the function returns `False`. Otherwise, it returns `True`. 

The provided code defines the `is_happy` function as requested. You can use it by providing a string as an argument to the function to check and return either `True` or `False` depending on the happy status of the string.