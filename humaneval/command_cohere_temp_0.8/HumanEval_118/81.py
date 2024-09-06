```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Make sure the word contains at least 2 characters
    if len(word) < 2:
        return ''

    # Count leading and trailing vowels
    leading_vowels = sum(1 for char in word[:2] if char in vowels)
    trailing_vowels = sum(1 for char in word[-2:] if char in vowels)

    # Base case
    if leading_vowels + trailing_vowels == 2:
        return word[1] if word[1] in vowels else ''

    # Count the number of pairs of consonants in the word
    pairs = sum(1 for i in range(1, len(word) - 1) if word[i] in consonants and word[i + 1] in consonants)

    if pairs == 0:
        return ''

    # Find the index of the closest vowel to the last pair of consonants
    curr_distance = float('inf')
    vowel_index = 0
    for i in range(1, len(word) - 1):
        if word[i] in consonants and word[i + 1] in consonants:
            curr_distance = 1 + abs(i - (len(word) - 2))
        if word[i] in vowels:
            curr_distance = min(curr_distance, abs(i - (len(word) - 2)), abs(i - 1 - (len(word) - 2)))
        if curr_distance == 1:
            vowel_index = i
    return word[vowel_index] if vowel_index != 0 else ''
```

This script assumes the input contains only letters, which is specified in the provided problem statement. It counts the leading and trailing vowels and uses these counts to determine if a vowel can fulfill the criteria. It calculates the index of the vowel closest to the last pair of consonants and returns it, or returns an empty string if no qualifying vowel is found. 

Let's break down the code step by step:
1. **Variable Declarations**: We start by defining the constants:
   - `consonants`: A string containing all English consonants, both lowercase and uppercase.
   - `vowels`: A string containing all English vowels, both lowercase and uppercase.

2. **Preconditions**: We first check if the length of the input word is greater than or equal to 2. This assumption is stated in the problem:
   ```python
   if len(word) < 2:
       return ''
   ```

3. **Leading and Trailing Vowels**: We calculate the number of leading and trailing vowels in the word. This is used to determine if the closest vowel should be considered based on the count of opening and closing vowels:
   ```python
   leading_vowels = sum(1 for char in word[:2] if char in vowels)
   trailing_vowels = sum(1 for char in word[-2:] if char in vowels)
   ```

4. **Base Case**: If there are 2 leading or trailing vowels, we return the vowel that is not counted in the leading or trailing vowels (i.e., the one in the middle):
   ```python
   if leading_vowels + trailing_vowels == 2:
       return word[1] if word[1] in vowels else ''
   ```

5. **Counting Consonant Pairs**: Here, we count the number of pairs of consonants in the word.