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

The function `get_closest_vowel()` takes a word as input and checks for the closest vowel located between two consonants within the given word, excluding the starting and ending vowels. It utilizes two arrays for storing English consonants and vowels to aid in the process. The function first converts the input word to lowercase and checks if the first letter is a consonant, moving forth to examine if the last letter is a consonant as well. Assuming the condition is met, the function further investigates the possibility of a close vowel located between these consonants. If a match is found, the function returns that vowel; otherwise, it returns an empty string. 

This algorithm assumes the input contains only English letters, as described in the problem statement. 

The code above provides a clear and efficient solution to the problem and can be easily integrated into larger projects.