import math
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: Number needs to checked
    :return: boolean
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    words = sentence.split(" ")
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result