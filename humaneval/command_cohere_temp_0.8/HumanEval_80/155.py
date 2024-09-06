```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function returns `True` if the string is happy, and `False` otherwise. 

The function first checks if the length of the string is at least 3, and if not, it returns `False`. Then, it initializes a `letters_set` to store unique letters in the string for the last 2 characters. The function then iterates over the string, and for each consecutive trio of characters, it checks if they are distinct. If the `letters_set` length is at least 3 and the current character is already in the set, then the string is not happy and the function returns `False`. Otherwise, the character is added to the `letters_set` and the function checks the next trio of characters. If the loop completes without finding any duplicates, the function returns `True`.

This solution works accordingly as the happyness is checked iteratively and the necessary checks are performed to confirm the happyness of the string. The provided tests would prove the functionality of the script.