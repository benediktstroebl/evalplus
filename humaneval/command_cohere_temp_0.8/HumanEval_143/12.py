```python
def is_prime(n):
    """
    Checks if a number is prime
    Returns true if n is prime, else false
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)
```

This code solves the problem by first splitting the sentence into words using the `split()` method. Then, it iterates over each word, checking if its length is prime using the `is_prime()` function. If the length is prime, it adds the word to the `result` list. Finally, it joins the words back into a single string and returns the result. 

The `is_prime()` function is included to check if a number is prime or not. It iterates from 2 to `sqrt(n)` and checks if any number in this range divides `n`, if any such number is found, the function returns `False`, otherwise, it returns `True`. 

Overall, the code efficiently solves the problem and meets the constraints.  Any improvements to the `is_prime()` function will depend on the size of the input as this one is efficient for its purpose and is compact in terms of lines of code.