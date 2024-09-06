Here's a Python script that defines a function `select_words()` to solve the problem you've described:
```python
def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    words = s.split()
    result = [word for word in words if len(word) == n and sum(1 for c in word if c in consonants) == n]
    return result if result else []
```

This script splits the input string into a list of words and then iterates through each word. It counts the number of consonants in each word and compares it to the target number of consonants `n`. If a word has exactly `n` consonants, it is added to the `result` list, which is returned if it's non-empty, and empty list is returned otherwise.

Let's break down the code step by step:
1. **Converting String to List of Words:**
   The first step is to split the input string `s` into a list of words, where each word is separated by a single space. This is done using the `split()` method, which splits the string on whitespace (including spaces). This list of words is stored in the variable `words`:
   ```python
   words = s.split()
   ```
2. **Counting Consonants:**
   To solve this problem, we need to count the number of consonants in each word. A consonant in the English alphabet is any letter that is not a vowel (including Y and W, which can function as consonants). The string `consonants` contains all the consonants in the English alphabet. We will use this string to count the consonants in each word:
   ```python
   consonants = 'bcdfghjklmnpqrstvwxyz'
   ```
3. **Filtering Words Based on Consonants:**
   We want to filter the words in the `words` list to find those that contain exactly `n` consonants. We use a list comprehension to iterate over each word in `words` and check two things:
   - `len(word) == n`: This checks if the length of the word is exactly equal to the target number of consonants `n`. This ensures we are considering exact matches.
   - `sum(1 for c in word if c in consonants) == n`: This counts the number of consonants in the word using a generator expression. It iterates through each character in the word and counts 1 if the character is in the `consonants` string. This count is then checked against the target number of consonants `n`.

   If both conditions are met for a word, it is included in the `result` list:
   ```python
   result = [word for word in words if len(word) == n and sum(1 for c in word if c in consonants) == n]
   ```
4. **Returning the Result:**
   After processing all the words, the `result` list is returned if it's non-empty. If no words match the criteria, an empty list is returned:
   ```python
   return result if result else []
   ```

This function `select_words()` takes an input string `s` and a target number of consonants `n` as arguments. It returns a list of words from the input string that contain exactly `n` consonants, in the order they appear in the string. If no such words are found, an empty list is returned.

This approach assumes that the input string contains only letters and spaces, as mentioned in the problem statement.