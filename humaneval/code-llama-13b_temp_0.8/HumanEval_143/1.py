
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
    primes = []
    for word in words:
        is_prime = True
        for i in range(2, int(len(word)/2)+1):
            if word[0] == 'a' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
                is_prime = False
                break
            if word[-1] == 'a' or word[-1] == 'i' or word[-1] == 'o' or word[-1] == 'u':
                is_prime = False
                break
            if word[0] == word[-1]:
                is_prime = False
                break
            if int(word) % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(word)
    return ' '.join(primes)

