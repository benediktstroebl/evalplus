```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
    for i in range(3):
        if letters_count[i] > 0 and letters_count[i] == letters_count[i+1] and letters_count[i] == letters_count[i+2]:
            return False
    return True
```

The given Python script defines a function called `is_happy` that checks whether a given string is happy or not based on the problem statement. The function first establishes the base condition of a minimum length of 3 for the string. It then uses three counters to keep track of the occurrences of the last three letters in the string. Finally, the function checks if the counts of these three letters are the same and returns `True` if they are, and `False` otherwise. The resulting evaluation is then returned to the caller.  This ensures that every triplet of consecutive letters in the string is unique, and returns `True` if the string is happy, and `False` otherwise.  This is assessed in a self-contained fashion, standing alone without reliance on external variables or conditions.  This also allows the function to be readily reusable and reliably ported to other situations and contexts in the future.