```python
def get_closest_vowel(word):
    cons_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char.isalpha():
            if char.lower() in vowels:
                if cons_count > 0:
                    return char
                else:
                    cons_count += 1
            else:
                cons_count += 1
        else:
            cons_count += 1
    return ''
```

The script counts consonants between vowels in the word provided. It uses a list of vowels ('a', 'e', 'i', 'o', 'u') to check if the next character is a vowel, incrementing a counter if it's a consonant. When the counter is 1, indicating a vowel, the script checks if the previous character was a consonant and returns it if so. The script returns an empty string if the word does not contain any instances of a single vowel surrounded by consonants. 

The word provided in the example induces a paradox where the first vowel 'o' is surrounded by consonants, however, it is also the first vowel in the entire word. The function will assume the empty string in this case.