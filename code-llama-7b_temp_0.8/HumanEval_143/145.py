
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
    #################
    # METHOD - 1
    #################
    # # Get all words from the sentence
    # words = sentence.split()

    # # A list to store prime numbers
    # primes = []

    # # Add all prime numbers to the list
    # for i in range(2, len(words) + 1):
    #     if not [j for j in range(2, i) if i % j == 0]:
    #         primes.append(i)

    # # Create an empty list to store output words
    # output_words = []

    # # Get the indices of all prime numbers
    # prime_indices = []
    # for prime in primes:
    #     prime_indices.append(primes.index(prime))

    # # Add the words at prime_indices to output_words
    # for index in prime_indices:
    #     output_words.append(words[index])

    # return " ".join(output_words)


    #################
    # METHOD - 2
    #################
    # Create a list to store output words
    output_words = []

    # Get all words from the sentence
    words = sentence.split()

    # Check if the length of a word is prime
    for word in words:
        if len(word) in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
            output_words.append(word)

    return " ".join(output_words)

