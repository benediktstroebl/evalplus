Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to be checked
    :return: boolean value based on primality
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    words = sentence.split(' ')
    ans = []
    for word in words:
        if len(word) == 1 or not is_prime(len(word)):
            continue
        ans.append(word)
    return ' '.join(ans)
```

This script includes a `is_prime` helper function to check if a number is prime or not. The `words_in_sentence` function splits the input sentence into words using space as a delimiter, then it checks each word's length iteratively, ignoring the single-letter words, and appends the words with prime lengths to the `ans` list. Finally, it joins the list of ans into a single string and returns it.