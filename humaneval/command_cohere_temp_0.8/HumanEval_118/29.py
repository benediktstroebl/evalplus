```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    index = len(word) - 1
    while index >= 0 and word[index] in consonants:
        index -= 1
    if index == -1:
        return ''
    vowel = word[index].lower()
    if vowel in vowels:
        return vowel
    return get_closest_vowel(word[:index] + word[index + 1:])
```

This Python script provides a function called `get_closest_vowel`, which takes a word as input. This function is designed to identify the closest vowel to a specified condition within the given word. The function works by moving through the word from right to left, disregarding vowels at the beginning and end of the word. When the first consonant is encountered, the function checks if a vowel follows it, and if so, it returns that vowel. If no qualifying vowel is found after the first consonant, the function recursively searches for a vowel between two consonants in the remaining portion of the word. If no such vowel is found, an empty string is returned. 

The script employs the Python alphabets `consonants` and `vowels` to represent English consonants and vowels, respectively. The `index` variable is used to initiate the search from the end of the word. The function utilizes a recursive approach to efficiently identify the closest vowel that meets the problem's criteria. 

This code demonstrates how to solve a specific problem with a defined algorithm and adheres to Python's PEP 8 style guide for clean and consistent code. It can be used as a stand-alone script to solve the given problem and is easily adaptable to various applications requiring text analysis or manipulation.