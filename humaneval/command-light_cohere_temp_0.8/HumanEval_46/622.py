```python
def fib4(n: int):
    """The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
    """
    numbers = [0, 1]
    for _ in range(n):
        number = numbers[-1] + numbers[-2]
        numbers.append(number)
    return number

# Test the function
test_number = int(input("Enter a test number: "))
result = fib4(test_number)
print(f"The result is: {result}")
```
In this Python script, the function `fib4` computes the n-th element of the Fibonacci sequence using an iterative approach. The function begins with an initial list `numbers` containing the first two numbers of the sequence (0 and 1). Then, it iterates through the input `n` until it finds the desired number. The result is then calculated by summing the last two numbers in the list and appending the result back into the list.