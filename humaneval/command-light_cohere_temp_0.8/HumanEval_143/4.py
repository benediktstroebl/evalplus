```python
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers, and the order of the words in the new string should be the same as the original one.

    Constraints:
        1. The length of the string and it only contains letters.
    2. The length of any maximum string must be a prime number.
    3. The output string must be a prime numbers only.
    """


Example:
sentence = "This is a test"
new_sentence = words_in_sentence(sentence)
print(new_sentence) # Output: "is"
```