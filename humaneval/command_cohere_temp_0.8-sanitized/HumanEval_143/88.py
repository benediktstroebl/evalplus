def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: Number to be checked.
    :return: True if n is a prime number, else False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    words = sentence.split() 
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)