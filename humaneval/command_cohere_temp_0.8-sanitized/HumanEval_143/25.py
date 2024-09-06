import re
from collections import Counter
def words_in_sentence(sentence):
    prime_words = []
    
    # Find words with prime lengths
    for word in re.findall(r'\b\w+\b', sentence):
        if is_prime(len(word)):
            prime_words.append(word)
    
    # Sort and join prime words to preserve original order
    sorted_prime_sentence = ' '.join(prime_words)
    
    return sorted_prime_sentence
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True