```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Finds and joins the words in a sentence with prime lengths
    """
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return ' '.join(prime_words)
```

This script includes the `is_prime` function for checking prime numbers, and the `words_in_sentence` function applies this check to sentence words and stitches together words with prime lengths. 

To ensure a more efficient prime-checking mechanism, the `is_prime` function utilizes a strategic range for the loop (from 2 to `int(n**0.5) + 1`) rather than a straightforward linear approach. This optimization takes advantage of the distribution of prime numbers. 

To clarify, the `int(n**0.5) + 1` term handles edge cases like `len(word)` being `1`, which would cause a divide-by-zero error with the initial `2` loop limit. 

The prime number check via the Sieve of Eratosthenes algorithm would be more fitting for a context involving large sets of numbers, but the linear approach is reasonably efficient for the scenario of checking numerous word lengths in a text. 

To obtain more concise prime words, you could opt for a more stringent prime check, for instance, by acknowledging only prime numbers that are 3 and above. 

I hope this solution aids your prompt! Let me know if you seek further refinement or would like to delve into another aspect of coding.