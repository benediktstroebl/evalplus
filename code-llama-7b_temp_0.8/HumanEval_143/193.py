
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
    # O(n) time | O(1) space
    if not sentence:
        return ""

    words = sentence.split(" ")
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    isPrime = lambda num: any(num % prime == 0 for prime in primes)
    return " ".join(filter(lambda word: isPrime(len(word)), words))

    """
    # O(nlog(n)) time | O(n) space
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    isPrime = lambda num: any(num % prime == 0 for prime in primes)

    def wordsLengths(words):
        return [len(word) for word in words]

    def filterWords(words, lengths):
        return filter(lambda idx: isPrime(lengths[idx]), range(len(words)))

    def wordsList(words):
        return list(map(lambda idx: words[idx], filter(lambda idx: isPrime(len(words[idx])), range(len(words)))))

    if not sentence:
        return ""

    words = sentence.split(" ")
    return " ".join(wordsList(words))
    """
