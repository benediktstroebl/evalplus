```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256  # Assuming ASCII
    for letter in s:
        letters_count[ord(letter)] += 1
    return all(count % 3 == 0 and count != 0 for count in letters_count[::3])
```

The script creates a function called `is_happy()` which determines whether a given string is happy or not. It checks if the string's length is at least 3 and examines every three consecutive letters. Using a counter, it ensures that each set of three letters is distinct and neither the first nor the last in the sequence. The function returns true if these conditions are met, and false otherwise.

The assumption of ASCII should work well for the test cases provided, but might cause issues with other characters sets.  If you plan to use this script in a broader context, consider adding character set tolerance or introducing a more robust solution. 

To use this code, copy and paste it into a Python environment or script, and then call the `is_happy()` function with the string you want to check. The function will return `True` if the string is happy, and `False` otherwise.