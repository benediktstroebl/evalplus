```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    """
    vowels = 'AEIOUaeiou'  
    concats = [c for c in word if c.isalpha()]
    ans = ''    
    for right_idx in range(len(concats) - 2, -1, -1):
        right_con = concats[right_idx]
        if right_con not in vowels:
            if ans == '':
                ans = right_con
            elif abs(vowels.find(ans) - vowels.find(right_con)) 
                < abs(vowels.find(ans) - vowels.find(concats[right_idx + 1])):
                ans = right_con    
    return ans
```
This approach uses a list comprehension to identify possible right consonants, then competitively selects the closest consonant to the previously identified vowel (or the first consonant if none are found). This competitive selection approach ensures the closest vowel to the right is picked.