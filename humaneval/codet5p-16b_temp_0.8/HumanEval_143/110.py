
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    from math import sqrt
    from string import ascii_lowercase

    words = sentence.split(' ')
    prime_numbers = []

    for word in words:
        length = len(word)

        if length > 2:
            is_prime = True
            for letter in ascii_lowercase:
                if sqrt(length) == int(sqrt(length)):
                    is_prime = False

            if is_prime:
                prime_numbers.append(word)

    return''.join(prime_numbers)
