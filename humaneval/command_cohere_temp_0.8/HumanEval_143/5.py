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

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    words = sentence.split()  # split the sentence into words
    prime_words = [word for word in words if is_prime(len(word))]  # check the length of every word
    return ' '.join(prime_words)  # join the prime words back into a string
```
The `is_prime` function checks if a number is prime using a predefined algorithm. The `words_in_sentence` function splits the input sentence into words and then checks the length of each word to see if it's prime. It then re-joins the prime word lengths to form a new string and returns the result.