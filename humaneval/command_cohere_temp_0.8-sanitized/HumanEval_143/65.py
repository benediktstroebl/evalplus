def is_prime(n):
    """
    Checks whether the integer is a prime or not.
    :param n: Integer to check whether it is prime or not.
    :return: True if n is a prime, else False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    words = sentence.split(' ')
    new_sentence = ''
    for word in words:
        if is_prime(len(word)):
            new_sentence += word + ' '
    return new_sentence[:-1]