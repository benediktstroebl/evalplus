Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to be checked
    :return: boolean value based on whether n is prime or not
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

    :param sentence: input sentence
    :return: string with words whose lengths are prime numbers
    """
    words = sentence.split(' ')
    new_sentence = ""
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence.strip()

# Example usage
sentence = "This is a test"
print(words_in_sentence(sentence))  # Output: "is"

sentence = "lets go for swimming"
print(words_in_sentence(sentence))  # Output: "go for"
```

This script includes the `is_prime` function for checking whether a number is prime or not. The `words_in_sentence` function splits the input sentence into words using space as a delimiter, then it checks whether the length of each word is prime and constructs a new sentence from those prime-length words, ensuring that the word order is preserved. The resulting script is self-contained and solves the problem as described in the prompt.