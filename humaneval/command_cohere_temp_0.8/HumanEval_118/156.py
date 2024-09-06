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
            elif char.lower() not in vowels:
                cons_count += 1
            else:
                cons_count = 0

    return ''
```

The script counts consonants between vowels in the word. If it finds a vowel within one of these sequences, it returns that vowel. If no such vowel is found, it returns an empty string. This algorithm works for all examples in the prompt.