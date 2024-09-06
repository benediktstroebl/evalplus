```python
def is_prime(n):
    """
    Checks whether the integer 'n' is a prime number or not.

    Args:
        n (int): Number to check if it is prime

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
        sentence (str): The input sentence with spaces separating words

    Returns:
        str: A sentence with words whose lengths are prime numbers.
    """
    
    words = sentence.split()  # Split the sentence into words
    
    prime_words = []  # List to store prime words
    
    for word in words:
        if is_prime(len(word)):  # Check if the length of the word is prime
            prime_words.append(word)  # Add the word to the list if it's prime
    
    return ' '.join(prime_words)  # Join prime words to form a new sentence
```

The `is_prime` function is used to determine if a given number is prime, and the `words_in_sentence` function splits the input sentence into words and then checks the lengths of each word before gathering the prime-length words into a new sentence.

This approach ensures that only the lengths of the words are considered for primality, not the actual words, which aligns with the intent of the provided code. 

This solution assumes the input constraints as provided in the problem statement.