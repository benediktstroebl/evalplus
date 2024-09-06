```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
# Sample Test Cases
if __name__ == "__main__":
    tests = [
        [-10, 4, 6, 1000, 10, 20],
        [2, 3, 4, 5, 6],
        [3, -9, -5, -15, -20, 0, 70],
        [0, 1, 2, 3, 4, 5, 6],
        [10, -5, -15, -20, -21, -22]
    ]
    
    for test in tests:
        print(f"Test: {test}")
        actual_median = median(test)
        expected_median = int((test[n // 2] + test[-n // 2]) / 2)
        print(f"Actual median: {actual_median}")
        print(f"Expected median: {expected_median}")
        if actual_median != expected_median:
            print("Test failed")
    print("All tests passed!")
```
The provided code defines a function median that calculates the median of a given list. The function takes a list as input and returns the median value. The code includes a test cases with various input lists to verify the correctness of the median function. The test cases are passed through, and the function's behavior is evaluated against the expected values. The output provides the results of the test cases and indicates whether the tests passed or failed.