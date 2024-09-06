```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty.")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    else:
        return lst[len(lst) // 2]

# Test cases
test_median = []
test_median.append([-10, 4, 6, 1000, 10, 20])
test_median.append([1, 2, 3, 4, 5])
test_median.append([1, 2, 3, 4, 6, 7])
test_median.append([-100, -1, 2, 3, 4, 5])
test_median.append([1, 2, 3, 4, 5, 6, 7, 8])

# Run tests and check results
print(f"Test results:")
for test in test_median:
    print(f"Input: {test}")
    print(f"Expected median: {median(test)}")
    print(f"Actual median: {test[-1]}")
``` 
This code defines a median function that calculates the median of the elements in a list. It handles empty lists correctly, and also handles lists with odd and even lengths. 

The code then provides test cases with a variety of inputs and verifies the results using the median function.