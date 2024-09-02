
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
    list_words = sentence.split()
    primes = filter(lambda x: x > 1, find_primes(len(list_words)))
    primes_set = set(primes)
    filtered_list = []
    for word in list_words:
        if len(word) in primes_set:
            filtered_list.append(word)
    return " ".join(filtered_list)

