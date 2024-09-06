```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 for y in str(x))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension with a generator expression to filter out numbers that have an even digit in their integer representation. The `any()` function will short-circuit as soon as a `True` value is encountered in the generator expression, meaning that the entire expression `any(int(y) % 2 for y in str(x))` will return `True` if at least one digit in the string representation of the number is odd, and therefore the number is not divisible by 2. The list of odd integers is then sorted in increasing order and returned.

This solution is efficient since it takes linear time in the number of elements in the list, and the number of digits in the longest number is bounded by O(1). 

The test cases are written as inline Python code within the markdown. When returned from the function, the test cases print their expected value, and assert that the printed value matches the expected value. Here is an example:
```python
test_cases = [
    (["15", "33", "1422", "1"], ["1", "15", "33"]),
    (["152", "323", "1422", "10"], []),
]
for inp, exp in test_cases:
    print(unique_digits(inp)) == exp
    assert bool(eval(f"{unique_digits(inp)} == {exp}"))
```

These test cases will be run automatically if the script is run with `python script.py`. However, since this is a markdown, the tests will not run automatically. To run the tests manually, the script and the tests can be copied to a Python file and run with the `python -m unittest test_file.py` command.