
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
    # TODO: write your code here
    # sort words by length
    # remove words with non-prime length
    # join words back together
    words_list = sentence.split(' ')
    prime_list = [len(word) for word in words_list if len(word) > 1 and all(i % word_len != 0 for i in range(2, word_len))]
    prime_list.sort()
    return ' '.join([words_list[i] for i in prime_list])

