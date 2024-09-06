Here's a self-contained Python script that defines a function string_sequence that returns a string containing space-delimited numbers starting from 0 up to a given n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + str_sequence(n - 1) + "}"

def str_sequence(n: int) -> str:
    return "".join(str(i) for i in range(n))

# Test cases
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(str_sequence(0), '')
assertEqual(str_sequence(1), '1')
assertEqual(str_sequence(9), '0 9')
```
The function str_sequence is a helper function that uses the range function to generate the sequence of numbers and then joins those with spaces to form a string. The function then returns the string_sequence(n) calls this helper function with the desired number of elements and returns the result as a string.