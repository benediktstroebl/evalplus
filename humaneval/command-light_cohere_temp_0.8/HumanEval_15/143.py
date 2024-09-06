Here is a Python script that contains a self-contained function that generates a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return " ".join([str(i) for i in range(n)])

# Test cases
test_seq = [
    (0, "0"),
    (5, "0 1 2 3 4 5"),
    (10, "0 10 20 30 40 50"),
    # Additional large n for future growth (feel free to add more)
    (100000, "0 1 00 10 100 200 300 400 500 600 700 800 900 1000"),
]

for test_case in test_seq:
    print(f"Test case: {test_case[0], '{test_case[1]}')")
    assert string_sequence(test_case[0]) == test_case[1]

# Main program
n = 10
print(f"String sequence for n={n}")
``` 
This code demonstrates the use of a self-contained function that generates a string of numbers from 0 to n, and provides test cases to validate the correctness of this function. 
Feel free to add more test cases or customize the behavior of your functions!