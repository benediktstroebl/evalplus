import string
from prime import is_prime
def words_in_sentence(sentence):
    words = sentence.split(' ')
    result = []

    for word in words:
        if is_prime(len(word)):
            result.append(word)

    return ' '.join(result)