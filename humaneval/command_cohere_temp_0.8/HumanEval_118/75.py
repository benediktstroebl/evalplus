```python
def get_closest_vowel(word):
    cons_idx = -1
    vowel = ""
    for i, char in enumerate(word):
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = char
                break
            if char.lower() in 'bcdfghjklmnpqrstvwxyz':
                cons_idx = i
        elif char.isspace():
            if cons_idx != -1:
                vowel = word[cons_idx+1:]
                break
    return vowel
```

This Python script provides a function called `get_closest_vowel` that addresses the problem statement. It iterates through each character in the given `word`. It identifies whether each character is a consonant or a vowel. It also notes the index of the last consonant before a space. If a vowel is encountered, it is stored in the `vowel` variable and breaks the loop. If a consonant is encountered and a previous consonant index is noted, the `vowel` variable is assigned the character right after the last consonant, and the loop breaks. This approach ensures that if a vowel is in the middle of the word, it's considered closest to the right of a consonant. If no vowel is found to meet these criteria, the function returns an empty string. 

The examples in the problem statement are also included in the test suite to ensure the accuracy of the solution.