```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = numbers.split()
    low = []
    for num in numbers:
        if num.isdigit():
            low.append(int(num))
    sorted_numbers = ' '.join(map(str, sorted(low))))
    return sorted_numbers

# Test cases
test_1 = "three one five"
test_2 = "zero six three"
test_3 = "two three seven"
test_4 = "five six eight"
test_5 = "four seven nine"

# Test Function Call
test_results = sort_numbers(test_1)
print("Test 1 Results:", test_results)

test_results = sort_numbers(test_2)
print("Test 2 Results:", test_results)

test_results = sort_numbers(test_3)
print("Test 3 Results:", test_results)

test_results = sort_numbers(test_4)
print("Test 4 Results:", test_results)

test_results = sort_numbers(test_5)
print("Test 5 Results:", test_results)
 ``` 
This script defines a function `sort_numbers` that takes a string of numbers separated by spaces and returns a sorted version of that string. The test cases include various strings representing sets of numbers, and the function is called with each test case. The output will be the expected to be the numbers sorted from smallest to largest.