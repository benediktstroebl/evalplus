```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.space_separated_numbers = sorted(map(int, numbers. cut numbers))
   return ''.join(numbers)

def test_sort_numbers():
    """ Test case function """
    test_list = ['three one five', 'zero two seven eight', 'five six three']
    expected = ['zero two seven eight', 'five six three']
    got = sort_numbers(test_list)
    assert got == expected, "test failed"

if __name__ == "__main__":
    print("Testing sort_numbers function...")
    test_sort_numbers()
```
This code defines a function sort_numbers that takes a space-separated string of numbers as input and returns a space-separated string with the numbers sorted from smallest to largest. The function utilizes the test_sort_numbers function to verify its correctness by passing a test case that contains a list of strings with different numbers and comparing the output against the expected output.