def is_prime(n):
    """
    A helper function to check if a number is prime or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split()
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)
    return " ".join(prime_words)
