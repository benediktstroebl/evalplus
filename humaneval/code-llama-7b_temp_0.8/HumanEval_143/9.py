
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
    # O(2^n)
    # O(n)
    # words = sentence.split(" ")
    # primes = [x for x in range(2,len(words)+1) if all([x % y != 0 for y in range(2,x)])]
    # return " ".join([words[i] for i in range(len(words)) if len(words[i]) in primes])

    # O(nlogn)
    # O(n)
    # words = sentence.split(" ")
    # primes = [x for x in range(2,len(words)+1) if all([x % y != 0 for y in range(2,x)])]
    # return " ".join([words[i] for i in range(len(words)) if len(words[i]) in primes])

    # O(nlogn)
    # O(n)
    primes = [x for x in range(2,len(sentence)+1) if all([x % y != 0 for y in range(2,x)])]
    return " ".join([sentence[i:j] for i in range(len(sentence)) for j in range(i+1,len(sentence)) if len(sentence[i:j]) in primes])

    # O(n)
    # O(n)
    # words = sentence.split(" ")
    # primes = [x for x in range(2,len(words)+1) if all([x % y != 0 for y in range(2,x)])]
    # return " ".join(list(filter(lambda x: len(x) in primes, words)))

    # O(n)
    # O(n)
    # words = sentence.split(" ")
    # primes = [x for x in range(2,len(words)+1) if all([x % y != 0 for y in range(2,x)])]
    # return " ".join(filter(lambda x: len(x) in primes, words))

    # O(n)
    # O(n)
    # words = sentence.split("
