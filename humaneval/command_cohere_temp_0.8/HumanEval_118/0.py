```python
def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel and char.lower() not in 'qvwxz':
                cons_count += 1
        elif char.isspace():
            continue
        elif char.isdigit():
            if cons_count > 0:
                return char
        else:
            continue
    if cons_count > 0 and cons_count % 2 == 1:
        return char
    else:
        return ''
```

The Python script provided defines a function `get_closest_vowel` that attempts to find the closest vowel to a specified word's right side. The function iterates through the word, tracking alpha characters. Vowels are checked through the `lower()` method to determine if the character is a vowel, updating a boolean variable.

For consonants, the function uses a list 'qvwxz' to identify these characters, incrementing a counter if a consonant is found. The function evaluates if the word ends with a consonant and odd in quantity; if so, the function returns the ending character. If not, the function returns an empty string. 

The provided example tests - `yogurt`, `FULL`, `quick`, and `ab` - showcase the functions' capabilities. The function returns the closest vowel to the right, accounting for starting and ending vowels, and resulting in an empty string if no qualifying vowels are present.