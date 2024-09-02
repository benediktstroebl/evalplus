
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
    # the problem statement is unclear on what exactly is expected of a prime number
    # my approach is to say we are looking for the first word in the sentence
    # which has a length of a prime number, then we look for the next one with the same length
    # then we look for the next one with the same length, etc
    words = sentence.split()
    i = 0
    while i < len(words):
        if is_prime(len(words[i])):
            return " ".join(words[i:])
        i += 1
    return ""

