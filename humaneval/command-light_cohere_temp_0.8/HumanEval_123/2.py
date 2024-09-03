```python
def get_odd_collatz(n):
    if n <= 1:
        return [n]
    sequence = [n]
    for _ in range(1, int(n**0.5) + 1):
        sequence.append(int(n% + n - 2))
    return list(sequence)[::-1]

def test_get_odd_collatz():
    print(get_odd_collatz(5))  # [1, 5]
    print(get_odd_collatz(10))  # [5, 6, 10, 9, 8, 7, 4, 3, 2, 1]
    print(get_odd_collatz(13))  # [8, 13, 21, 20, 11, 14, 9, 5, 6, 7, 10, 16, 8, 4, 2, 1]
```

The code defines a function `get_odd_collatz` that takes an integer `n` as input and returns a list containing the odd numbers in the Collatz sequence for the given `n`. The function starts with an initial list containing `n`, and iterates to append subsequent odd numbers in the sequence until the length of the list reaches the value of `n**0.5` or bare metal, there is no check on this number, which will cause an error. 

This function is then tested using the `test_get_odd_collatz` function, which simply prints the results of the `get_odd_collatz` function for a series of test cases.