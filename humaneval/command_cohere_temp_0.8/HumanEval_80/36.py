```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    letters_set = set()
    letters_set_size = 0
    for letter in s:
        letters_count[ord(letter)] += 1
        letters_set.add(letter)
        letters_set_size += 1
        if letters_set_size == 3:
            if len(letters_set) == 1:
                return False
            else:
                letters_set.clear()
                letters_set_size = 0
    return True
```

The script employs a counter and a set to check if each 3 consecutive letters in the string are distinct. The counter array `letters_count[ord(letter)] += 1` keeps track of the frequency of each letter in the string, while the set `letters_set` stores only unique letters. The variable `letters_set_size` keeps the size of the set, which is used to determine the number of unique letters present.

In each iteration of the loop, the script checks if the size of the set is equal to 3, representing 3 consecutive letters. If so, the set is cleared, and `letters_set_size` is reset to 0 to account for the next sequence of letters.

The function returns True if all subsets of length 3 have distinct letters and False otherwise.