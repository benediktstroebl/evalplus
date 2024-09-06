Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```
The above method uses the translate method to remove vowels from the text. The str.maketrans method is used to create a translation table that removes all vowels, and the translate method is then used to apply this translation to the input string. Note that the translation is case-sensitive, so it will remove vowels regardless of case. The function will remove intra-word vowels, as well as extra vowels at the start or end of the string.