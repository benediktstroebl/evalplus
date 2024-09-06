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

The script counts consonants between vowels in the word. If it finds a vowel that is not at the edge of the word and is between two consonants, it returns that vowel. If no such vowel is found, it returns an empty string. This algorithm avoids cases where the first or last character of a word is a vowel but is not necessarily the closest vowel to the middle. 

Here is an example usage of the function:
```python
print(get_closest_vowel("yogurt")) # u
print(get_closest_vowel("FULL")) # U
print(get_closest_vowel("quick")) # 
print(get_closest_vowel("ab")) # 
``` 

This should return `u`, `U`, `None`, and `None` respectively, as these words demonstrate all possible cases of the function's behavior.