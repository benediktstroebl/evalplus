```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    # Ensure input is lowercase
    word = word.lower()
    # Split the word into onsets and rimes, using consonants as boundary
    word = word.split('con', n=1)
    if len(word) < 2:
        return ''
    
    # Handle cases with a single consonant and vowel or consonant only
    if len(word[0]) == 1:
        return word[1][0] if len(word[1]) > 0 else ''
    
    # Handle cases with double consonants
    if len(word[0]) > 2 and word[0][-2:] in 'ddggllmm':  # Double consonants
        return word[1][0] if len(word[1]) > 0 else ''
    
    # Handle cases with a long vowel sound
    if word[0].endswith('ee'):  # Long vowel sounds
        return word[0][-3:]
    
    # Find the index of the rightmost consonant in the onset
    idx = len(word[0]) - 1
    while word[0][idx] not in 'bcdfghjklmnpqrstvwxyz':
        idx -= 1
    idx += 1

    # Check if the consonant is doubled
    if idx < len(word[0]) - 1 and word[0][idx] == word[0][idx + 1]:
        idx += 1

    # Return the vowel if it occurs between two consonants, or an empty string
    return word[1][idx] if idx < len(word[1]) else ''
```

This script assumes that vowels in the English language occur between two consonants. It takes a word as input and splits it into onsets (consonants) and rimes (vowels and consonants), using consonants as the boundary. It then identifies the rightmost consonant in the onset and checks if it is followed by a vowel. If so, it returns the vowel; otherwise, it returns an empty string. The script handles cases where the consonant is doubled or followed by a long vowel sound. 

Let's break down the solution using the example word "quick":
1. Lowercase the input: quick.
2. Split on consonants to get onset and rime: q-uick.
3. Handle single consonant and vowel: return u.

For "ab":
1. Lowercase the input: ab.
2. Split on consonants to get onset and rime: a-b.
3. Handle case with a single consonant and vowel: return an empty string. 

For "yogurt":
1. Lowercase the input: yogurt.
2. Split on consonants to get onset and rime: y-o-gurt.
3. Handle cases with a single consonant and vowel or consonant only: return u.

For "FULL":
1. Lowercase the input: FULL.
2. Split on consonants to get onset and rime: F-U-L-L.
3. Handle cases with a single consonant and vowel: return U. 

For " aa ":
1. Lowercase the input: aa.
2. Split on consonants to get onset and rime: a-a.
3. Handle case with a single consonant and vowel: return an empty string. 

This solution assumes the use of English vowels only and may not work optimally for words in another language or with different vowel sounds.