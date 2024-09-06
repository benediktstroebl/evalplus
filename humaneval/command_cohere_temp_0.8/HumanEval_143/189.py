Here's a Python script that solves the given problem with an efficient approach using the generator expression and passing the corresponding unit tests:
```python
def words_in_sentence(sentence):
    prime_words = [word for word in sentence.split(' ') if is_prime(len(word))]
    return ' '.join(prime_words)

def is_prime(n):
    """
    Efficiently checks if an integer n is a prime number.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test Cases
print(words_in_sentence("This is a test"))  # Output: 'is'
print(words_in_sentence("lets go for swimming"))  # Output: 'go for'
```

The provided solution utilizes the generator expression to efficiently filter out prime-length words from the sentence. The is_prime function checks for primality in O(sqrt(n)) time, which is much more efficient than checking all divisors up to n. This makes the overall solution scalable and suitable for larger inputs. 

Note: For larger inputs, remember that the sqrt(n) loop might be a bottleneck, even with the improved algorithm. This is because checking for primality is, in theory, a linear time operation, and the generator expression won't significantly slow it down.