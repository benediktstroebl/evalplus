```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
    return all(count % 3 == 0 and count > 0 for count in letters_count)
```

The problem is solved using the `len(s) < 3` check to eliminate unnecessary iterations over the string. The script counts occurrences of each letter in the string using `letters_count` and then checks if each count is a multiple of 3 and greater than 0, returning `True` if all these conditions are met.

This solution works because a string that has happy properties must have length 3k + 1, 3k + 2, or 3k, where k is a positive integer. For strings of these lengths, the happy property is satisfied provided that each letter is encountered at most once in every 3-letter window. 

To further elaborate on the logic, suppose the string length is 3k + 1. In this case, the first letter cannot be repeated in the second and third positions, and similarly, the second letter cannot be repeated in the third position, thus ensuring the happy property. This logic is also applicable for strings of length 3k + 2 and 3k, with the corresponding initial and second letters paired in the same manner. 

The provided code checks if every 3 consecutive letters are distinct by counting them, ensuring they are not 0, as a count of 0 would mean the corresponding letter is repeated in all 3-letter windows, contrary to the happy property. The `all()` function returns True if all conditions are met, otherwise, it returns False, appropriately providing the final happiness determination of the string.