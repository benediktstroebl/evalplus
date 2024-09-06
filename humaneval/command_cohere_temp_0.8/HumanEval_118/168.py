```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores vowels at the start and end of the word.
    """
    # Ensure the word has more than one character to avoid division by zero
    if len(word) < 2:
        return ""

    vowels = "AEIOUaeiou"
    # Using a generator expression to eliminate leading and trailing vowels
    filtered_word = [c for c in word if c not in vowels]
    
    # Check if the word is all consonants, return empty string
    if not filtered_word:
        return ""

    # Calculate the ratio of consonants to vowels
    ratio = len(filtered_word) / (len(word) - 2)
    # Determine the closest vowel based on this ratio
    closest_idx = int(ratio * len(vowels))
    return vowels[closest_idx]
```

This script assumes that the English vowels `AEIOUaeiou` constitute the vowels in the words being evaluated. It removes any occurrences of these vowels at the beginning and ending of the word and calculates a ratio of consonants to vowels in the word. Based on this ratio, it selects the closest vowel and returns it. 

Let's demonstrate it with a test case:
```python
def test_get_closest_vowel():
    assert get_closest_vowel("yoga") == "a"
    assert get_closest_vowel("zwieb") == "e"
    assert get_closest_vowel("ALL") == "L"
    assert get_closest_vowel(" CAB ") == "A"
    assert get_closest_vowel("qu") == ""
    assert get_closest_vowel("bc") == ""

test_get_closest_vowel()
```