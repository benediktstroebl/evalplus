def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to be checked
    :return: boolean value based on primality
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    words = sentence.split(' ')
    ans = []
    for word in words:
        if len(word) == 1 or not is_prime(len(word)):
            continue
        ans.append(word)
    return ' '.join(ans)