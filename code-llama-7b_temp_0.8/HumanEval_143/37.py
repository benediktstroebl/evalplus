
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
    # We can create a list of all prime numbers < 100, then compare each word's length to that list,
    # if the word's length is prime then we can add it to a new list
    # Finally, we can return the joined string of the new list
    # O(n) time | O(n) space - where n is the length of the sentence
    # Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

    # create a list of all prime numbers < 100
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # split the sentence into words
    words = sentence.split()

    # create an empty list to store the output words
    output_words = []

    # iterate through the words
    for word in words:
        # if the length of the word is in the list of primes
        if len(word) in primes:
            # add the word to the output
            output_words.append(word)

    # return the joined string of the output words
    return ' '.join(output_words)
