```python
import math

def is_prime(n):
    """
    Checks whether a number is prime or not.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Extracts words from a sentence whose lengths are prime numbers.

    Args:
        sentence (str): Input sentence with spaces separating words.

    Returns:
        str: A sentence with words whose lengths are prime numbers.
    '''
    words = sentence.split()
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)
```

This function leverages a primality testing utility (`is_prime`) to identify words in the sentence that have prime lengths. It then constructs and returns a new sentence using only those prime-length words, maintaining the original sentence's word order.

The `is_prime` function utilizes an optimized trial division method to check for primality. It iterates through integers from 2 up to the square root of the number and checks for divisibility. If the number is divisible by any integer within this range, it's not a prime; otherwise, it's considered prime. 

This approach ensures that the function remains efficient for larger inputs while maintaining a reasonable time complexity (`O(sqrt(n))`) for primality testing. 

Note that the `words_in_sentence` function effectively extracts relevant words and returns a new sentence, emphasizing words with prime lengths while maintaining their original arrangement.