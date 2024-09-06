Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

To test the function, a main method is added to execute the tests:
```python
def main():
    tests = [
        (-12, 1, 1),
        (123, 1, 2),
        (10, 2, 0),
        (21, 1, 1)
    ]
    for num, expected_even, expected_odd in tests:
        result = even_odd_count(num)
        assert result == (expected_even, expected_odd)

if __name__ == "__main__":
    main()
```

The even_odd_count function uses two variables to count the number of even and odd digits, respectively. A loop is used to convert the number to a string and iterate through each digit. The modulus operator is used to determine if each digit is even or odd. The main method executes the tests and verifies the results.