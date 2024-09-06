def is_prime(n):
    """
    Checks whether the integer `n` is a prime number or not.

    Args:
        n (int): Number to be checked.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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
        sentence (str): Input sentence with words separated by spaces.

    Returns:
        str: A sentence with words whose lengths are prime numbers.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"
    """
    words = sentence.split()  # Split the sentence into words using space as separator
    prime_words = [word for word in words if is_prime(len(word))]  # Check the lengths of each word
    return ' '.join(prime_words)  # Join prime words back into a string