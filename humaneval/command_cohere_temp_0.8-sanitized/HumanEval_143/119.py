def is_prime(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): Number to check if prime or not.

    Returns:
        bool: If the number is prime or not.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Args:
        sentence (str): A string representing a sentence with spaces.

    Returns:
        str: A new sentence with words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """

    words = sentence.split(" ")
    prime_words = []

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return " ".join(prime_words)