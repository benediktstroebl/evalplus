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
        sentence (str): A string representing a sentence with words separated by spaces.

    Returns:
        str: A string containing words with prime lengths from the original sentence.
    """ 
    words = sentence.split()  # split the sentence into words using space as separator
    prime_words = []  # a list to store prime words
    
    for word in words:
        if is_prime(len(word)):  # check if the length of the word is prime
            prime_words.append(word)  # add the word to the list if it's prime
    
    return ' '.join(prime_words)  # join the prime words to form a string and return
```

The provided solution utilizes the `is_prime` helper function to determine whether a number is prime. This function recursively checks divisibility for numbers from 2 to the square root of the number. The `words_in_sentence` function splits the input sentence into words based on spaces and then assesses each word's length for primality. If a word has a prime length, it is added to the `prime_words` list. Finally, the function rejoins the prime words into a single string, which is then returned as the output.

Note: For optimal performance, it is recommended to set a maximum limit for primality testing to the square root of the number. This approach significantly reduces the number of iterations required for checking divisibility, resulting in a more efficient solution.