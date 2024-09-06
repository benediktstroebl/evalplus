```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256  # Assuming ASCII
    for letter in s:
        letters_count[ord(letter)] += 1
    return all(count % 3 == 0 and count > 0 for count in letters_count[::3])
```

The happyness of the string is evaluated solely based on the parity of the count of each letter, every 3 letters. If the parity is always even (count is divisible by 3 and counts are greater than 0) then the string is deemed happy. The function starts by assuming that all counts are 0 and builds up the counts as it iterates through the string.

This solution has a time complexity of O(N) where N is the length of the string and a space complexity of O(1) as it only uses a single 256-element array.