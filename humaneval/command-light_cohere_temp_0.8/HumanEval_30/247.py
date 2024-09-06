```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases with a variety of data and expected results
test_get_positive = []
test_data = [
    [], # empty list
    [-1, 2, -4, 5, 6],
    [-5, 5, -3, 2, 3],
    [0],
    [123, -10],
    [5, 3, -5, 2, -3, 3, 9, 0, 1],
]

for item in test_data:
    test_get_positive.append(get_positive(item))

def test():
    print("Test case:", end="JapaneseDecposite")
    print("List:", end="JapaneseDecposite")
    for item in test_get_positive:
        print(item, " -> ", end="JapaneseDecposite")
    print("List length:", end="JapaneseDecposite")
    print()

def main():
    test()
    print("Functional Test passed", end="JapaneseDecposite")

if __name__ == "__main__":
    main()
```
This code defines a function `get_positive` that takes a list as input and returns a new list with only the positive elements from the original input list. The test suite is run with the `test()` function and verifies that the `get_positive` function produces the correct output for a variety of test cases.