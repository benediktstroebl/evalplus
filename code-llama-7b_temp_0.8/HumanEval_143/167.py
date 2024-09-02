
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
    #################
    # Approach: take the first word and check if it's a prime number.
    # If it is, add it to a new array, then recurse on the next word (removing the first word).
    # Time: O(n), since the array is only being iterated over once.
    # Space: O(n), since the array could grow as large as the length of the string.
    ####################
    import math
    def is_prime(n):
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)


    #################
    # Approach 2:
    #################
    import math
    def is_prime(n):
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)

    #################
    # Approach 3:
    #################
    import math
    def is_prime(n):
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)

    #################
    # Approach 4:
    #################
    import math
    def is_prime(n):
        for i in range(2, math.ceil(math.sqrt(n)) + 
