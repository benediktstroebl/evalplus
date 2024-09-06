import re
from sympy.primerange import prime
from sympy.ntheory import isprime
PRIMES = [str(p) for p in prime(100)]
def words_in_sentence(sentence):
    words = re.findall(r'\w+', sentence)
    prime_words = [word for word in words if word in PRIMES and isprime(int(word))]
    return ' '.join(prime_words)