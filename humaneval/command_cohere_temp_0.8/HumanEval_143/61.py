Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.
    """
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()

# Example Usage
sentence = "This is a test"
print(words_in_sentence(sentence))  # Output: "is"

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Output: "go for"
```

This script includes a `is_prime` function that checks whether a given number is prime or not. The `words_in_sentence` function splits the sentence into words, and then iterates through the words, checking each word's length with the `is_prime` function. If the length is prime, the word is added to the `result` string. Finally, the `result` string is returned with the words of prime lengths.