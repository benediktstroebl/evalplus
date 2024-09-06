```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 up to including n."""
    return ' '.join(map(str, range(n+1)))
```

This problem can be solved using the range function in Python which creates a sequence of numbers starting from 0 up to including n. Then, this sequence is converted into a string using map and join functions. Such conversion assigns each number in the sequence to a string representation, separating them using spaces.

This approach ensures the string_sequence function is efficient as it employs native Python functionalities, opting for simplicity and readability over using a list comprehension. The function is also robust, handling the edge case where n is 0, gracefully.