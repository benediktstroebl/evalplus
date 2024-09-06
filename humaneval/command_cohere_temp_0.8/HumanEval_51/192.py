Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

The function removes vowels from the input text using the `translate` method and provides translations for removing both lowercase and uppercase vowels. It returns the modified text without vowels. The tests provided ensure that different scenarios are correctly handled, including empty strings, different text lengths, and varying vowel patterns.

The code explanation:
1. The function `remove_vowels(text)` takes a single argument `text`, which is the input string from which vowels will be removed.
2. The string `"aeiouAEIOU"` is stored in the variable `vowels`. This string contains all lowercase and uppercase vowels.
3. The `translate()` method is used on the `text` string with `str.maketrans("", "", vowels)` as the translation mapping.
   - `str.maketrans("", "", vowels)` creates a translation map that maps each character in `vowels` to `None`. This means that all vowels will be replaced with `None` in the mapping.
4. The `translate()` method scans the `text` string character by character and replaces each vowel with `None` from the mapping.
   - The result is a new string where all vowels have been removed.
5. The modified string is returned, and the input text without any vowels is displayed.