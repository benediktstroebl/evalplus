```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
    for i in range(3):
        if letters_count[i] > 0 and letters_count[i] == letters_count[i-1] == letters_count[i+1]:
            return False
    return True
```

The given Python script defines a function `is_happy` that checks if a given string is happy. It first verifies if the string's length is at least 3. If not, it returns `False`, since there cannot be any consecutive groups of 3 distinct letters. If the length is at least 3, it proceeds to loop through the string, tracking the count of each letter in a list `letters_count`. After counting, it checks every trio of consecutive letters, ensuring that each group is distinct and none repeat the count of the previous or next group. If all are distinct, it returns `True`, and if any trio is not, it returns `False`. The script provides an accurate and efficient solution to determine if a string is happy or not.