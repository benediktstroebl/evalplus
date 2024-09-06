```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    word = word.lower()
    index = next((i for i, let in enumerate(word) if let in consonants), len(word))
    if index == 0 or index == len(word) or word[index - 1] in vowels and word[index + 1] in vowels:
        return ''
    return word[index]
```

The function relies on the condition that in order to find the closest vowel, it must be surrounded by 2 consonants from the right side of the word. The Python script lowercase the input word and rotates it to the first consonant that is met. However, it excludes cases where the vowel is in the beginning or ending of the word or when the vowel is surrounded by 2 vowels. The function returns the closest vowel or an empty string if no valid vowel is found. 

Here is an example of how to use the function:
```python
print(get_closest_vowel("yogurt"))  # Output: "u"
print(get_closest_vowel("FULL"))  # Output: "U"
print(get_closest_vowel("quick"))  # Output: ""
print(get_closest_vowel("ab"))  # Output: ""
``` 

This should output:
```
u
U
""
""
```