```python
def count_up_to(n):
    """Return an array of the first n integers that are prime numbers and less than n"""
    limit = n + 1
    prime_numbers = []
    for num in range(2, limit):
        is_prime = True
        for p in range(2, int(num ** 0.5) + 1):
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers

# Unit tests
test_count_up_to = []
test_cases = [
    (5, []),
    (11, [2,3,5,7]),
    (0, []),
    (20, [2,3,5,7,11,13,17,19]),
    (1, []),
    (18, [2,3,5,7,11,13,17])
]

for test_case in test_cases:
    test_count_up_to = count_up_to(test_case[1])
    assert test_count_up_to == test_case[2], f"Failed for {test_case[0]}: {test_case[2]} != {test_count_up_to}"

# Output printed for debugging
print("Testing count_up_to function:")
```
The function count_up_to is a self-contained Python script that implements a function that takes a non-negative integer n and returns an array of the first n integers that are prime numbers and less than n. The function uses a array comprehension and a for loop to iterate through the numbers from 2 up to the given n, checking each number to see if it is prime using a nested for loop. 

The function is then passed to a series of unit tests, with the test cases being a tuple of the number of elements to test and the expected output of the function for that number of elements.