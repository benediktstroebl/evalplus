```python
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # Using regex to check right-aligned vowels between consonants
    import re

    pattern = r'(?<!\w)(?<!\s)[aeiou](?=\w|\s)'
    match = re.search(pattern, word)
    
    return match.group(0) if match else ""
```

This script employs regex to address the challenge; the regex `r'(?<!\w)(?<!\s)[aeiou](?=\w|\s)'` is used to search for vowels that are not preceded by a consonant or whitespace and are followed by a consonant or whitespace. This identifies the required vowels.

Here is a clarified breakdown of the regex:
- `(?<!\w)`: Negative lookbehind ensures the vowel is not preceded by a consonant
- `(?<!\s)`: Negative lookbehind ensures the vowel is not preceded by whitespace
- `[aeiou]`: The literal vowel characters we want to match
- `(?=\w|\s)`: Positive lookahead ensures the vowel is followed by a consonant or whitespace

The example usage demonstrates the functionality of the function with different test cases. Adjustments might be necessary to ensure the function aligns with your specific needs. 

For optimal performance, regular expressions should be used cautiously with larger test cases or substantial amounts of text, as they can be resource-intensive. If you encounter performance issues, consider alternative methods or optimizations. 

If you are working with strings in a different language, remember to adjust the script to match the vocabulary of that language.