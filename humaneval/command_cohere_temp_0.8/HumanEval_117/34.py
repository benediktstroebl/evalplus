Here's a Python script that contains a function called `select_words` which solves the problem you've described:
```python
def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    words = [word for word in s.split(' ') if word]
    return [word for word in words if len(set(word) & consonants) == n]
```
This script will return a list of all words contained in the string `s` that contain exactly `n` consonants, in order these words appear in the string `s`. The list will be empty if no words match this criteria. The script assumes the input string contains only letters and spaces.

Let's break down the code step-by-step:
1. **Consonant Dictionary:**
   ```python
   consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
   ```
   This dictionary stores all the consonants in lowercase. The presence of each consonant will be checked against the characters in a word to determine if it's a consonant.

2. **Splitting into Words:**
   ```python
   words = [word for word in s.split(' ') if word]
   ```
   This line splits the input string `s` into individual words using spaces as separators. It uses a list comprehension and ignores any empty words (produced by trailing or leading spaces).

3. **Filtering Words by Consonants:**
   ```python
   return [word for word in words if len(set(word) & consonants) == n]
   ```
   Here, we use another list comprehension to filter the words based on the presence of exactly `n` consonants. 
   - `set(word)` converts the word into a set of characters, which removes any duplicate characters. 
   - `set(word) & consonants` produces a new set that contains characters present in the word but only consonant characters. 
   - `len(...)==n` checks if the new set has exactly `n` elements, which indicates the word has exactly `n` consonants.

This script will return the list of words from the input string that contain exactly `n` consonants as described in the prompt.