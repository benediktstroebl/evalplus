```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    vowels = 'IEOUaeiou'  
    # Regular expression to match a consonant that is not the last letter
    regex = '[^%s%s]' % (word[0], word[-1])
    
    matches = [m for m in word[1:-1].lower().replace(' ', '').replace('-', '').replace('&', '').split('&') if m in vowels and re.search(regex, m)]
    if matches:
        return matches.pop()
    else:
        return ''
```

The solution utilizes regular expressions to identify suitable vowels amidst the word's body, eschewing the beginning and concluding vowels. Subsequently, it retrieves and returns the closest vowel among these identified vowels, assumed to be sandwiched between two consonants. 

Here is an example of a test case:
```python
test_cases = [
    ('yogurt', 'u'),
    ('FULL', 'U'),
    ('quick', ''),
    ('ab', ''),
    ('ABC', ''),
    ('B&W', ''),
    ('PlayStation', 'a'),
]

for word, expected in test_cases:
    assert get_closest_vowel(word) == expected
```

This test suite validates the function against a range of scenarios, ensuring it returns the expected closest vowels or an empty string when no qualifying vowels are found.