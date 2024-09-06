```python
def get_closest_vowel(word):
    """
    Find the closest vowel to the right of the word, if there is one between two consonants.
    """
    vowels = 'AEIOUaeiou'  
    ll = len(word) 
    k = len(word) - 1 
    while k >= 0 and word[k] in 'QWERTYUIOPASDFGHJKLZXCVBNM' : 
        if word[k] in vowels : 
            if word[k-1] in 'QWERTYUIOPASDFGHJKLZXCVBNM' : 
                return word[k] 
        k -= 1 
    return ''
```
The function cycles through the word using a while loop, starting from the end and moving backward. 

It checks whether the current character is a consonant and, if so, it checks whether the character before it is a vowel. 

If both conditions are met, it returns the current character. If it reaches the beginning without returning, it returns an empty string. 

The code works under the assumption that consonants in the English alphabet are 'QWERTYUIOPASDFGHJKLZXCVBNM' and vowels are 'AEIOUaeiou'. 

This approach is case-sensitive, as specified in the prompt.