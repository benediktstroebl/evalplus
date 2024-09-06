```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    # Omit the first and last character since they are easiest to fulfill
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i-1] in consonants and word[i+1] in consonants:
            return word[i]
    return ''
```

This approach uses two dictionaries for a more efficient check. The dictionary vowels contains the vowels ('aeiouAEIOU'), and consonants list the consonants ('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'). The first and last characters are checked to see if they are vowels or consonants, and if they are consonants, it verifies whether the middle character is a vowel. If all these criteria are met, it returns the middle character, and if none are met, it returns an empty string. 

Here is an example usage of the function with a test case: 
```python
print(get_closest_vowel("abacus")) # Output: 'a'
```

This tests the function on the word "abacus," which has a vowel in the middle, and should return the closest vowel, 'a'. 

This problem can be approached in many different ways, but this solution demonstrates an efficient and elegant approach. Let me know if you would like any alterations to the code!