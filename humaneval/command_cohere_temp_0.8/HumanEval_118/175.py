```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    # Count index from right for each consonant and store the maximum
    max_consonant_index = max(list(word.lower()).index(c) for c in consonants if c in word)
    # Count index from right for each vowel and store the minimum
    min_vowel_index = min(list(word.lower()).index(v) for v in vowels if v in word and word[len(word) - len(v):].lower() != v)
    # Return the vowel that is closest to the maximum consonant index
    if min_vowel_index != -1 and max_consonant_index != len(word) - 1:
        return word[len(word) - min_vowel_index - 1 : len(word) - max_consonant_index - 1]
    else:
        return ""
```

The approach for this solution is to enumerate all vowels and consonants in the word, determining the indices of the rightmost consonants and the leftmost vowels. The rightmost consonant's index is taken as the maximum index, while the leftmost vowel's index is considered the minimum. The vowel closest to the maximum index is returned if they intersect; otherwise, an empty string is returned. 

This algorithm has a time complexity of O(n) where n is the length of the word, as it requires iterating over the characters once and analyzing their indices.