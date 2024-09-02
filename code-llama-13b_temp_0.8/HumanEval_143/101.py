
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
    # Reshet words in sentence
    words = sentence.split()
    # Create prime numbers array
    prime = []
    # Fill prime array
    for i in range(1, 100):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
    # Create filtered words array
    filtered = []
    # Fill filtered array with prime words
    for word in words:
        if len(word) in prime:
            filtered.append(word)
    # Create result string
    result = ""
    # Fill result string with filtered words
    for word in filtered:
        if result:
            result += " " + word
        else:
            result = word
    # Return result
    return result

