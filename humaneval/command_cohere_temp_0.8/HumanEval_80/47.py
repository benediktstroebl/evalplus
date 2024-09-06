```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(3, len(s), 3):
        if len(set(s[i:i+3])) != 3:
            return False
    return True
```

The problem is defined such that a string is happy if its length is at least 3 and every 3 consecutive letters are distinct. To solve this, the script starts by checking if the string length is at least 3, using `len(s) < 3`. If not, the string is not happy, so the function returns `False`. This check prevents us from having to check a string less than 3 characters in length, which can't possibly be happy. 

If the string length is at least 3, we then proceed to check every 3 consecutive letters to see if they are distinct. To do this, we create a set of letters from the first 3 characters (`letters_set = set(s[0:3])`). Then, we iterate through the string 3 letters at a time (`for i in range(3, len(s), 3)`), check if the set of these letters is of size 3 (`if len(set(s[i:i+3])) != 3`), and if it's not, the string is not happy, and we return `False`. If we make it through the entire string without returning `False`, the string is happy, and we return `True`. 

By structuring the code this way, we avoid unnecessary computations and navigate through the string efficiently, checking every 3 letters to see if they're distinct, ultimately leading to a happy result.