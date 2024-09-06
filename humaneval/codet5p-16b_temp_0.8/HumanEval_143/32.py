
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

    words = sentence.split(' ')
    primes = []
    result = ""
    for word in words:
        if len(word) == 1:
            continue
        if len(word) not in primes:
            primes.append(len(word))
    primes = sorted(primes)
    for p in primes:
        for word in words:
            if len(word) == p:
                result += word
                result +=''
    return result[0:len(result)-1]
