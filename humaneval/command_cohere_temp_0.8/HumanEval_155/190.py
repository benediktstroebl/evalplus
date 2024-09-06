Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the count of even and odd digits in num, respectively:
```python
def even_odd_count(num):
    count = 0
    num_str = str(num)
    for char in num_str:
        if char > '9':
            continue
        if char % 2 == 0:
            count += 1
        else:
            count += 1
    return count, count
```

To test the function, a main method is added to conduct several tests with different inputs and print the expected outputs.

```python
def main():
    tests = [
        (-12, (1, 1)),
        (123, (1, 2)),
        (10, (2, 0)),
        (107, (2, 5)),
        (15, (1, 4)),
    ]

    for num, expected in tests:
        actual = even_odd_count(num)
        print(f"For num {num}, expected {expected}, actual {actual}")

if __name__ == "__main__":
    main()
```

When running the script, it will output the expected count of even and odd digits for different inputs and the actual values computed by the even_odd_count function.