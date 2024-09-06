```python
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that 
    stands between two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # Use a dictionary to check if next char to right is a consonant
    word = word.lower()
    char_dict = {
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1
        }
    );
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for char in word:
        if char in vowels:
            if count == 1:
                return char
            count = 0
        elif char_dict.get(char, None) and count == 0:
            count = 1
        elif char_dict.get(char, None) and count == 1:
            return ''
    return ''
```

This code defines a function `get_closest_vowel` that takes in a word as an argument and returns the closest vowel to the right side of the word that is sandwiched between two consonants. The function checks each character in the word, maintaining a count of consecutive consonants. When a vowel is encountered and the count is 1, it returns that vowel. If a vowel is encountered when the count is greater than 1, it returns an empty string as there are no vowels between two consonants beyond that point. When a consonant is encountered and the count is 1, it resets the count to 0, as the consonant breaks the consecutive run of consonants. The overall time complexity of this code is `O(n)`, where `n` is the length of the given word, as it iterates through each character in the word once. 

Here are some example test cases to verify the functionality of the code:
```python
test_cases = [
    ("yogurt", "u"),
    ("FULL", "U"),
    ("quick", ""),
    ("ab", ""),
    ("aab", "a"),
    ("iiiiii", "i"),
    ("zzzzzz", ""),
    ("liek", "e"),
]

for case in test_cases:
    assert get_closest_vowel(case[0]) == case[1]
```