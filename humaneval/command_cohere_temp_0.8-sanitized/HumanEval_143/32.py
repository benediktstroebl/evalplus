import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    words = sentence.split(' ')
    res = []
    for word in words:
        if is_prime(len(word)):
            res.append(word)
    return ' '.join(res)