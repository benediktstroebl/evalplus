Here's a Python script with a self-contained function that solves the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))
```

This removes vowels (both uppercase and lowercase) from the input text using the `translate` method with a translation table created using `str.maketrans`. The empty translation string ensures that other characters remain unchanged. The function still handles edge cases, such as handling an empty input string and maintaining non-vowel characters. 

Here's the markdown code block with the updated Python script to solve the problem:
```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return text.translate(str.maketrans("", "", vowels))

```