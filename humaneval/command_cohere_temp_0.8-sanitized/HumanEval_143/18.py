def is_prime(n):
    """
    Checks whether the integer 'n' is prime or not.
    :param n: Integer to be checked whether it's prime
    :return: True if n is prime, else False
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    words = sentence.split(' ')
    res = []
    for word in words:
        if len(word) == 1 or not is_prime(len(word)):
            continue
        res.append(word)
    return ' '.join(res)