
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
    words = [word for word in words if len(word) > 0]
    filtered_words = []
    for word in words:
        is_prime = True
        num = len(word)
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            filtered_words.append(word)
    new_string = ""
    for word in filtered_words:
        new_string += word
    return new_string