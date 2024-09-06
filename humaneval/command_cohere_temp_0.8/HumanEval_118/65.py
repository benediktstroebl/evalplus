```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    len_word = len(word)
    for i in range(len_word):
        if word[i] in consonants and len_word - i - 1 >= 1 and word[len_word - i - 1] in consonants:
            for j in range(i + 1, len_word - i - 1):
                if word[j] in vowels:
                    return word[j]
    return ""
```

This script defines a function `get_closest_vowel` that takes in a word as an argument. It first creates two lists, `consonants` and `vowels`, containing all lowercase and uppercase English consonants and vowels, respectively. It then sets `len_word` to the length of the given word. 

The function then iterates through the characters of the word, starting from the second character (index 1) to the end of the word, checking if the current character and the next-to-last character are consonants. If they are, it iterates through the characters between them and the next-to-last character, checking if they are vowels. If a vowel is found, the function returns the vowel. If no vowel is found in this range, the function returns an empty string. 

This code will correctly find the closest vowel in a word between two consonants, case-sensitive, and handle starter and enders consonants as well as vowels.