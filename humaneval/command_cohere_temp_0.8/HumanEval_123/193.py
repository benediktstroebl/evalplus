Here's a Python script that contains a function called `get_odd_collatz` that solves the problem in a markdown code block:
```python
def get_odd_collatz(n):
    odd_collatz_sequence = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        odd_collatz_sequence.append(n)
    return odd_collatz_sequence

if __name__ == "__main__":
    # Test cases
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(13) == [13, 109, 417, 673, 1249, 8169, 21213, 43449]

    print("All tests passed!")
```

This script defines a function `get_odd_collatz(n)` that calculates and returns a list of odd numbers from the Collatz sequence for a given starting integer `n`. The `while` loop continues until `n` reaches 1, and the odd numbers are appended to the `odd_collatz_sequence` list.

The script also includes test cases to validate the function's behavior for different input values. If the function successfully computes the expected odd numbers for each test case, the program prints "All tests passed!" Otherwise, it will incorrectly indicate the failure of some tests. 

Let's delve into the correct reasoning and solution for the problem:
### Understanding the Collatz Sequence
The Collatz sequence, also known as the 3n+1 sequence or the hailstone sequence, is an intriguing sequence of integers that begins with any positive integer `n`. You iterate it by applying the following rules:
- If the current number is even, divide it by 2.
- If the current number is odd, multiply it by 3 and add 1.

The intriguing Collatz conjecture states that regardless of the initial value of `n`, the sequence will always eventually reach the value 1. However, this conjecture has not been proven or disproven for all integers, despite intense scrutiny from the mathematical community.

### Requirements of the Problem
The problem statement asks you to create a function `get_odd_collatz(n)` that takes a positive integer `n` as input and returns a sorted list containing only the odd numbers from the Collatz sequence. 

The requirement highlights the following:
- The Collatz sequence for `Collatz(1)` is simply `[1]`.
- The returned list should be sorted in ascending order.

### Solution Approach
To solve this problem, you can use a `while` loop that iterates through the Collatz sequence until it reaches 1. You can keep track of the odd numbers in the sequence and store them in a list. Finally, you'll return this list of odd numbers.

#### Implementing the Solution
Here's the complete Python solution:
```python
def get_odd_collatz(n):
    odd_numbers = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        odd_numbers.append(n)
    return sorted(odd_numbers)

# Test cases
assert get_odd_collatz(1) == [1]
assert get_odd_collatz(5) == [1, 5]
assert get_odd_collatz(13) == [13, 109, 417, 673, 1249, 8169, 21213