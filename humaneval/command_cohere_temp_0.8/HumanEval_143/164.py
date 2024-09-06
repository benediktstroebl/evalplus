Here's a Python script that solves the given problem with an example:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.

    Args:
        n (int): Number to check if prime

    Returns:
        bool: True if n is prime, False otherwise
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
        sentence (str): A sentence with spaces separating words

    Returns:
        str: A new sentence with words whose lengths are prime numbers

    Examples:
    Input: sentence = "This is a test"
    Output: "is"

    Input: sentence = "lets go for swimming"
    Output: "go for"
    """
    words = sentence.split(' ')
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```

The provided example yields the following results:
```
Input: sentence = "This is a test"
Output: "is"

Input: sentence = "lets go for swimming"
Output: "go for"
```

The `is_prime` function checks whether a given number n is prime or not. It iterates from 2 to n's square root and checks if n is divisible by any number in that range. If it's not divisible by any, then n is declared prime. The `words_in_sentence` function splits the input sentence into words based on spaces and then checks each word's length for primality. If a word's length is prime, it's added to a list that's later joined back to form the desired output.