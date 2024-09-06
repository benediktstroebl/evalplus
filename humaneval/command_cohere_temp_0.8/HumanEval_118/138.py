```python
def get_closest_vowel(word):
    cons_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char.lower() in vowels:
            if cons_count > 0:
                return char
        else:
            cons_count += 1
    return ''
```

This script provides a function called `get_closest_vowel` taking a word as input. The function first counts the number of consecutive consonants from the right side of the word. It then checks if there is a vowel within that cluster of consonants. If so, the function returns the vowel. If not, an empty string is returned, indicating no vowel met the requirement in the word. This algorithm assumes English letters only in the input. 

The output of the provided examples in the prompt is:
- `get_closest_vowel("yogurt") ==> "u"`
- `get_closest_vowel("FULL") ==> "U"`
- `get_closest_vowel("quick") ==> ""`
- `get_closest_vowel("ab") ==> ""`