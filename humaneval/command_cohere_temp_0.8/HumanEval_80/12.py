```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
    return all(count < 3 for count in letters_count)
```

This script defines a function called `is_happy` that takes a string as an input and checks whether it is happy or not. 

Here's how it works:
1. If the string's length is less than 3, it is not happy anyway, so the function returns False.
2. A counter 'letters_count' is used to count how many times each letter appears in the string.
3. The final result is calculated by looping over the counts of each letter in 'letters_count' and returning 'True' only if all of them are less than 3.

This algorithm efficiently solves the problem in a concise manner.