```python
def get_closest_vowel(word):
    cons_idx = -1
    vowel = ""
    for i, char in enumerate(word):
        if char.is consonant():
            if cons_idx == -1:
                cons_idx = i
            elif char.is vowel():
                vowel = char
                cons_idx = i
        else:
            cons_idx = -1
    return vowel
```

This approach uses a simple loop to find the closest vowel to the right of the word, assuming that vowels in the beginning and ending don't count. The loop checks each character of the word and uses a `cons_idx` variable to track the rightmost consonant's index. When a consonant is found, the `cons_idx` is updated to its index, but when a vowel is found, the `vowel` variable is updated and the `cons_idx` is reset to -1, to restart the search for the next consonant. When the loop completes, the `vowel` variable will hold the value of the closest vowel to the right of the last consonant in the word, or an empty string if no such vowel is found.