def is_prime(n):
    """
    Checks whether the number is prime or not.

    Args:
        n (int): Number to check if prime or not.

    Returns:
        bool: True if n is prime, False otherwise.
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
        str: A string containing words whose lengths are prime numbers.

    Example:
        Input: sentence = "This is a test"
        Output: "is"
    """

    # Split the sentence into words using space as the delimiter
    words = sentence.split()
    result = []

    for word in words:
        # Check if the length of the word is prime
        if is_prime(len(word)):
            result.append(word)

    return " ".join(result)