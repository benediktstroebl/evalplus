```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    named_arr = [Names[int(i)] for i in sorted_arr if 1 <= int(i) <= 9]
    return named_arr

def main():
    Names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    test_cases = [
        ([2, 1, 1, 4, 5, 8, 2, 3], ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]),
        ([], []),
        ([1, -1 , 55], ["One"]),
    ]
    for inputs, expected in test_cases:
        result = by_length(inputs)
        if result == expected:
            print("Passed test")
        else:
            print("Failed test")

if __name__ == "__main__":
    main()
```

The function by_length sorts the array, reverses it, and then assigns names to the digits. The main function provides the `Names` dictionary and executes a series of tests to verify the correct behavior of the function. If the output of the by_length function matches the expected output, the test is considered passed, otherwise, it is considered a failure.  The code will print "Passed test" or "Failed test" depending on if the test cases passed or not.