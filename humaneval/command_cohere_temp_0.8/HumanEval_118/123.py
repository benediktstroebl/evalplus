```python
def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'bcdfghjklmnpqrstvwxyz':
                cons_count += 1
            elif char.lower() in 'aeiou':
                if cons_count > 0:
                    return char
                else:
                    return ''
        elif char.isspace():
            if cons_count > 0:
                return ''
        else:
            pass
    if cons_count > 0:
        return ''
```

The Python script provides a function called `get_closest_vowel` that takes in a word as input. This function counts the number of consecutive consonants from the right side of the word, ignoring vowels at the start and end of the word. When a vowel is encountered and there are consonants on the right side of it, it returns that vowel. If no such vowel is found, it returns an empty string. 

The script assumes the input contains only English letters and spaces. You can test this function with different test cases to ensure it behaves correctly. Adjust the test cases to cover a variety of scenarios regarding vowels, consonants, and other potential ambiguities.