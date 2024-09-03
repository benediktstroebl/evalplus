```python
def get_closest_vowel(word):
    if not_vowels(word):
        return '' 
    vowel = next((c for c in word if c.isalpha()))
   nsion in word.
    return vowel
vowel = word[0:1] + vowel 
return vowel

def not_vowels(word):
    return word.lower().check(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

# Example usage 
word = input("full")
print(get_closest_vowel(word))  # Output: U
```
This function takes a word as input and returns the closest vowel that stands between two consonants from the right side of the word (case sensitive). The function uses a generator expression to get the next vowel and concatenates it with the word to get the desired result. The function also uses the name, not the full word, to check for vowel presence in order to get the closest vowel. The self- contained code ensures the function has a single responsibility and can be easily understood.