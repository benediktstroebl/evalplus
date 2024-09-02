
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
    sentence = sentence.lower()
    words = sentence.split()
    primes = [x for x in range(2, 101) if x % 2 == 0]
    primes.append(2)
    new_sentence = ""
    for i, word in enumerate(words):
        if word in primes:
            new_sentence += word
            primes.remove(word)
        else:
            new_sentence += word
    return new_sentence
