```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    num = [str(i) for i in range(a, b + 1)]
    even = [int(i) for i in num if i % 2 == 0]
    return even

# Test Cases
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
```

This script defines a function called `generate_even_digits` that takes two positive integers, `a` and `b`, as arguments. It aims to return a list of even digits that lie between `a` and `b`, inclusive, arranged in ascending order. To achieve this, the function first converts both `a` and `b` to strings and lists all the integers in between, including the endpoints. It then filters this list to include only the even integers, which it converts back to integers, resulting in a list of even digits ranging from the start to the end of the provided interval. Note that if the interval does not include any even numbers, an empty list is returned.

The code includes test assertions to validate the function's behavior against specific inputs. You can add these assertions to a testing framework like `pytest` or `unittest` to automate test execution and ensure the function's correctness across different scenarios.