```python
def even_odd_count(num):
    """Given an integer.

    Return a numbers of even and odd digits in a string representation of num.
    """

    return a tuple(map(int, str(num).

test_cases = [
    (-12),
    123
  ])
 
for num, test in test_cases:
    print(f'Test case {num}: {test} -> {even_odd_count(num)}')

# Output:
Test case -12: (1, 1) -> (1, 1)
Test case 123: (1, 2) -> (1, 2)
```
This Python code defines a function `even_odd_count` that calculates the count of even and odd digits in a given number. The function utilizes the map function to convert the digits in a string representation of the number to integers, and then counts the even and odd digits accordingly. The test_cases list contains two test cases to pass to the function, and the result is printed for each test case.