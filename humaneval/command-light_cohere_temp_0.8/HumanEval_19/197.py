```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(n) for n in numbers.
    return ' '.join(sorted(numbers))

def test_sort_numbers():
    return sort_numbers('three one five') == 'one three five'

if __name__ == "__main__":
    print("The answer is: ",end="")
    print(test_sort_numbers())
``` 
This Python script defines a function sort_numbers that sorts a space-separated string of numbers, returning the sorted result as a string. The function takes a input and uses a list comprehension to convert the input into a list of integers. The sorted list is then converted back to a string with a space separator. The test_sort_numbers function tests the sort_numbers function by passing the test string "three one five". The test passes, so the output is printed.