Here's a self-contained Python function that generates a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return " ".join([str(i) for i in range(n)])

# Test cases
test_seq = [
    (0, "0"),
    (5, "0 5 6 7 8 9"),
    (10, "0 9 1 2 3 4 5 6 7 8 9"),
    # Add more test cases as needed
]

test_seq()

```
The function uses the list comprehension to create a string containing numbers from 0 to n, with space delimiters. This code is can be expanded to handle larger ranges of numbers or to add additional formatting as needed.