
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
    num_words = len(words)
    num_primes = 0
    new_words = []
    for i in range(num_words):
        if words[i].isdigit():
            continue
        for j in range(i + 1, num_words):
            if words[j] == ' ' or words[j] == '-' or words[j] == '1' or words[j] == '2' or words[j] == '3':
                continue
            if not words[j].isdigit():
                break
            num_primes += 1
            prime = True
            for n in range(num_primes - 1):
                if (j - n) % words[j] != 0:
                    prime = False
                    break
            if prime:
                new_words.append(words[i])
    return ''.join(new_words)