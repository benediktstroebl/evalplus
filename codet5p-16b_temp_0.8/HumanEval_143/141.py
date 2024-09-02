
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

    words = sentence.split()
    prime_lengths = []

    for word in words:
        length = len(word)

        if length == 1:
            continue

        for i in range(2, length):
            if length % i == 0:
                break
        else:
            prime_lengths.append(length)

    output = ""

    for word in words:
        for prime_length in prime_lengths:
            if len(word) == prime_length:
                output += word
                break
            else:
                output += word + " "

    return output.strip()
