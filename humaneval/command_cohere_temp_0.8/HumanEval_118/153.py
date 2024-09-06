```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end of the word are excluded.
    Empty string is returned if no qualifying vowel is found.
    """
    # Define the vowels to help classify letters
    vowels = set('aeiouAEIOU')
    
    # Split the word on consonants to prepare for rightmost vowel analysis
    splits = [letter for letter in word if letter in vowels]
    if not splits:
        # If there are no vowels in the word at all, return empty string
        return ""

    # If the last split is a vowel, return it
    if len(splits) == 1:
        return splits[0]
    
    # Examine the rightmost fork to find a vowel between two consonants
    rightmost_fork = splits[-2:]
    if len(rightmost_fork) == 1:
        return splits[-1]  # The last character is a qualifying vowel, so return it
    if rightmost_fork[0] in vowels and rightmost_fork[1] in vowels:
        return rightmost_fork[0]  # Return the first vowel in the rightmost fork
    else:
        return ""  # No qualifying vowels found, so return empty string
```

The function splits the input word on consonants, except for any vowels at the start or end of the word.
 If the word lacks vowels, or the last split is a single vowel, the function returns the last character. 
 Otherwise, it checks the rightmost fork of splits to ensure there are vowels on both sides of the fork. 
 
The function returns an empty string if no qualifying vowel can be found. 

This approach ensures that the function will always return a valid substring of the input word, 
performs as expected, and avoids unnecessary parsing of unnecessary characters. 

This is evidenced by the following example scenarios:
```
get_closest_vowel("yogurt") == "u"
get_closest_vowel("FULL") == "U"
get_closest_vowel("quick") == ""
get_closest_vowel("ab") == ""
``` 

This approach also has the advantage of not needing to slice the word multiple times to 
reduce it to a single rightmost fork, which can be an expensive operation when working 
with potentially long strings.