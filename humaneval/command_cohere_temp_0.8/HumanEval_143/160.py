Here's a Python script that solves the given problem with an efficient approach using the `primality` library:
```python
import re
from sympy.primerange import prime
from sympy.ntheory import isprime

PRIMES = [str(p) for p in prime(100)]

def words_in_sentence(sentence):
    words = re.findall(r'\w+', sentence)
    prime_words = [word for word in words if word in PRIMES and isprime(int(word))]
    return ' '.join(prime_words)
```

The script utilizes the `sympy` library for primality testing and primerange generation up to 100, which are stored in the PRIMES list. It uses a regular expression to extract words from the sentence and then checks if each word is in the PRIMES list and is prime using the isprime function. Finally, it joins the prime words with spaces to form the desired output.