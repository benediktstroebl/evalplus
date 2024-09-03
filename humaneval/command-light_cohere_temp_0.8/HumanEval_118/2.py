```python
def get_closest_vowel(word):
    consonants = word[0:-1] + [word[-1]]
    vowels = "aeiouAEIOU"
    return vowels[min(consonants.index(c) -index(vowel) + 1) : len(vowels) - 1]

# Test cases
test_cases = [
    ("ab", ""),
    ("quick", "u"),
    ("full", "U"),
    ("yogurt", "u"),
    ("Hello", ""),
    ("world", "")
]

for test in test_cases:
    print(get_closest_vowel(test))
```
This code defines a function `get_closest_vowel` that aims to find the closest vowel that lies between the two consonants on the right side of a given English word, excluding the beginning and ending characters. The function creates a list of consonants using the characters excluding the beginning and ending of the word, and then uses the `min` function along with the `index` function to find the index of the closest vowel within the `vowels` string, ensuring that the vowel lies between the consonants on the right side of the word.

Finally, the code provides a set of test cases to verify the correctness of the function.