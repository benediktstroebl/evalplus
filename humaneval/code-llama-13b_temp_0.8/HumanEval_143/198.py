
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
    # Remove punctuations
    sentence = ''.join([i for i in sentence if i.isalpha()])
    # Remove extra spaces
    sentence = sentence.split()
    # Find prime numbers
    prime_numbers = [i for i in range(1, 101) if is_prime(i)]
    # Find the numbers whose length is prime number
    prime_length_numbers = []
    for i in range(len(sentence)):
        if len(sentence[i]) in prime_numbers:
            prime_length_numbers.append(i)
    # Create the string
    result = ''
    for i in range(len(prime_length_numbers)):
        result += sentence[prime_length_numbers[i]]
        if i < len(prime_length_numbers) - 1:
            result += ' '
    return result

