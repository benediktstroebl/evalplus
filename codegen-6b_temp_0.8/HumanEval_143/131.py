
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
    # abcdefghijklmnopqrstuvwxyz
    # "This is a test" -> "This is"
    # "lets go for swimming" -> "go for"
    # "a b c" -> "a"
    # "a"*2 -> "a"
    # "a"*3 -> "baa"
    # "a"*6 -> "aaaaaaaaaaaaaaaaa"
    # "a"*7 -> "aaaaaaaaaaaaaaaaaaaaa"
    # "a"*8 -> "aaaaaaaaaaaaaaaaaaaaa"
    # "a"*9 -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+1) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+2) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+3) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+4) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+5) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+6) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+7) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+8) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+9) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+10) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+11) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # "a"*(9+12) -> "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    # get the list of words from the sentence
    strings = sentence.split()
    primes = []

    for word in strings:
        # add the word to the primes if it is greater than 0 and less than 100
        if is_prime(len(word)):
            primes.append(word)

    # create the result string
    result = ""