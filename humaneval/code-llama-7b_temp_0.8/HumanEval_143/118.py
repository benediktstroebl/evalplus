
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
    # Your code here
    # first, we need to generate all the prime numbers
    primes = []
    n = 2
    while n <= 100:
        # is n prime?
        # first, we need to check if it is not divisible by any number before n
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
        n += 1
    
    # second, we need to extract the words from the sentence
    words = sentence.split()

    # third, we need to check if the word's length is a prime number
    result = ""
    for word in words:
        if len(word) in primes:
            result += word + " "
    return result.strip()
