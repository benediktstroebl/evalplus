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

This Python script defines a function called `is_happy` that takes a single argument - a string `s`. This function returns True if the string is happy, and False otherwise. The string is considered happy if its length is at least 3 and every set of 3 consecutive letters are distinct. The function checks if the length of the string is at least 3 using the `len()` function and returns False if it's shorter than 3. Then, it uses a set `letters_set` to store the letters encountered, iterating through the string with a range of len(s)-2 to exclude the last two characters. If the set size reaches 3 and the current character is already present in the set, it returns False, indicating that 3 consecutive letters are repeated. Otherwise, it adds the current character to the set and continues iterating. The function returns True at the end if no repeated consecutive triples are found.

The markdown code block shows the code without any syntax errors and is ready to be executed.