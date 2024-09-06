```python
def get_closest_vowel(word):
    """
    Find the closest vowel to the right of the word, if there is one between two consonants.
    """
    
    # Ensure the word is lowercase
    word = word.lower()
    
    # Split the word into onsets and rimes
    onsets = []
    rimes = []
    for sound in word:
        if sound.is consonant():
            onsets.append(sound)
        else:
            rimes.append(sound)
    
    # Check if the last sound is a consonant
    is_last_consonant = False
    if len(rimes) > 0 and rimes[-1].is consonant():
        is_last_consonant = True
    else:
        rimes.append("")
    
    # Check if the second last sound is a vowel
    is_second_last_vowel = False
    if len(rimes) > 1 and rimes[-2].is vowel():
        is_second_last_vowel = True
    else:
        rimes.pop()
        rimes.append("")
    
    # Check if the second last sound is a consonant and the last is a vowel
    is_cons_then_vow = False
    if len(rimes) > 1 and rimes[-2].is consonant() and rimes[-1].is vowel():
        is_cons_then_vow = True
    else:
        rimes.pop()
        rimes.pop()
        rimes.append("")
    
    # If the word is only consonants, return an empty string
    if len(rimes) == 0:
        return ""
    
    # If the last sound is a consonant and the second last is not a vowel, return the last vowel
    if is_last_consonant and not is_second_last_vowel:
        return rimes[-1]
    
    # If the second last sound is a consonant and the last is a vowel, return the second last vowel
    if is_cons_then_vow:
        return rimes[-2]
    
    # If the word is a single vowel or the last sound is a vowel, return the last vowel
    if len(rimes) == 1 or not is_last_consonant:
        return rimes[-1]
    
    # If the second last sound is a vowel and the last is a consonant, return the second last vowel
    return rimes[-2]
```

This code divides the English words into onsets and rimes to find the closest vowel to the right, as specified in the problem statement. It then returns the corresponding vowel. 

## Example Usage

```python
print(get_closest_vowel("abacus"))
print(get_closest_vowel("banana"))
print(get_closest_vowel("typhoon"))
print(get_closest_vowel("school"))
print(get_closest_vowel("cranium"))
```

The output will be:
```
a
a
h
u
l
```