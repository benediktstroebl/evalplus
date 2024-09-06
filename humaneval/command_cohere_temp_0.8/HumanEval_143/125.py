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
    words = sentence.split(' ')
    new_sentence = ''
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence.strip()

# Example Usage
sentence = "This is a test"
print(words_in_sentence(sentence))  # Output: "is"

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Output: "go for"
```

This script includes the `is_prime` function for checking whether a number is prime or not. The `words_in_sentence` function splits the input sentence into words separated by spaces, and then iterates through these words, adding them to a new string only if their length is prime. The resulting string is then returned.