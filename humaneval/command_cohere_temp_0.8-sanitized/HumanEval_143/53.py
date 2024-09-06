import string
from prime import primegen
def words_in_sentence(sentence):
    words = sentence.split(' ')
    prime_words = []

    for word in words:
        # Generate a prime number sequence up to the length of the word
        primes = primegen(len(word), 2)
        
        # Check if the word is made up of prime letters only
        if set(primes) == set(map(bool, word)):
            prime_words.append(word)

    return ' '.join(prime_words)
sentence = "This is a test"