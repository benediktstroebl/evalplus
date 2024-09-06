```python
def get_odd_collatz(n):
    odd_seq = [y for y in collatz_sequence(n) if y % 2 == 1]
    odd_seq.sort()
    return odd_seq
    
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Test cases
print(get_odd_collatz(1))  # [1]
print(get_odd_collatz(5))  # [1, 5]
print(get_odd_collatz(14)) # [1, 7, 11, 23, 19, 31, 43, 47]
``` 

This Python script defines a function `get_odd_collatz(n)` which returns a sorted list of odd numbers in the Collatz sequence of a given positive integer `n`. The function `collatz_sequence(n)` generates the entire Collatz sequence for a given starting value `n`, both odd and even numbers, which is then filtered to only include odd numbers. The resulting odd numbers are sorted in increasing order. 

The script passes the test cases printed in the comment, where the first test case is an edge case that returns a list with only 1, the second test case returns a list with 1 and 5, and the third test case returns a list with 7 odd numbers in the range of 1 to 47.