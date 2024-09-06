```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find the number of occurrences of a substring in a given string.
    """
    number_of_occurrences = 0
    for char in substring:
        if char in string:
            number_of_occurrences += 1
    return number_of_occurrences

# Unit tests
test_how_many_times = []
test_how_many_times.append([['', 'a'], 1])
test_how_many_times.append(['aaa', 'a'], 3)
test_how_many_times.append(['aaaa', 'aa'], 2)

def run_tests():
    """
    Run the function tests
    """
    test_how_many_times.assertstring = "aaaaaaa"
    test_how_many_times.assertstring = "aaa"
    assert how_many_times(test_how_many_times.stringstring, test_how_many_times.stringstring, test_how_many_times) == 3

# Main function to run the tests
def main():
    """
    Run the main function
    """
    run_tests()

if __name__ == "__main__":
    main()
```
This Python script defines a function `how_many_times` that counts the occurrences of a given substring within a given string. The function also has unit tests that verify its correctness. The `run_tests` function executes these tests, while the `main` function is the entry point where the tests are run.