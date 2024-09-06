```python
def is_prime(n):
    """
    Checks whether the integer `n` is a prime number or not.

    Args:
        n (int): Number to be checked.

    Returns:
        bool: True if n is prime, False otherwise.
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

    Args:
        sentence (str): The input sentence with spaces.

    Returns:
        str: A sentence with words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """

    words = sentence.split(' ')
    result = []

    for word in words:
        if is_prime(len(word)):
            result.append(word)

    return ' '.join(result)
```

This code first splits the input sentence into individual words based on the space character. Then, it checks the length of each word to see if it's a prime number using the `is_prime` function. If a word has a prime length, it's added to the `result` list. Finally, the function joins the prime words back into a single string to form the desired output sentence.