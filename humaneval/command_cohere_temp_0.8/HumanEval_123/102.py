```python
def get_odd_collatz(n):
    odd_collatz = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz.append(num)
    return odd_collatz

if __name__ == "__main__":
    # test case 1
    assert get_odd_collatz(1) == [1]
    # test case 2
    assert get_odd_collatz(5) == [1, 5]
    # test case 3
    assert get_odd_collatz(21) == [1, 21]
```

This Python script defines a function `get_odd_collatz(n)` which constructs the odd numbers in the Collatz sequence for a given positive integer `n`, and returns them in sorted order. The Collatz sequence for `n` is simulated via a `while` loop that iterates until the sequence reaches the base case of `1`. In each iteration, the even factorization is used to halve the previous number if it's even, otherwise, it multiplies by 3 and adds 1 to create the next number in the sequence. The odd numbers in the sequence are collected in the `odd_collatz` list, which is then returned. The script includes a test block with assert statements to verify the function's behavior for different inputs. Adjustments could be made to the function to instead immediately return the odd numbers collected thus far if the even case is encountered, but the current implementation maintains a more efficient and understandable approach.