
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
    sentence = sentence.split()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    for x in range(len(primes)):
        if primes[x] > len(sentence[0]):
            primes.append(primes[x])
            break
    
    for x in range(len(primes)):
        if primes[x] > len(sentence[1]):
            primes.append(primes[x])
            break
    
    for x in range(len(sentence)):
        if len(sentence[x]) in primes:
            return sentence[x]
