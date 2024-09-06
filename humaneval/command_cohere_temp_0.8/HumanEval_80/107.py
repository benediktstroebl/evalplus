```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrence = {}
    for i in range(len(s) - 2):
        first_letter = s[i]
        second_letter = s[i + 1]
        third_letter = s[i + 2]
        if (first_letter, second_letter, third_letter) in letters_occurrence:
            return False
        letters_occurrence[(first_letter, second_letter, third_letter)] = True
    return True
```

This code defines a function `is_happy` that takes a string `s` as input and checks whether it is happy as defined in the problem statement. It does so by performing the following steps:
1. It checks if the string's length is at least 3 using the `if` statement and returns `False` immediately if this condition is not met.
2. It initializes a dictionary called `letters_occurrence` to keep track of the occurrences of every set of three consecutive letters in the string.
3. The loop goes through each set of 3 consecutive letters in the string, excluding the last section (as it's not prudent to consider an incomplete set).
4. Within the loop, the three letters are extracted and uniquified using the tuple `(first_letter, second_letter, third_letter)` as keys in the `letters_occurrence` dictionary.
5. If the combination of letters has already been encountered, it means the string is not happy, and the function returns `False`.
6. If the loop completes without encountering any duplicate combinations, the string is happy, and the function returns `True`.

This solution follows the grammatical correctness of the test cases and should be able to pass the associated tests. 

This script can be run directly with Python in the command line by simply typing `python` followed by the asterisk `*` symbol to execute the script.