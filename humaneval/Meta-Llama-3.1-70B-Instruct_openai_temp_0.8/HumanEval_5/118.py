```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
assert intersperse([], 4) == []
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
assert intersperse([10, 20, 30, 40], 5) == [10, 5, 20, 5, 30, 5, 40]
print("All test cases pass.")

if __name__ == "__main__":
    numbers = [input("Enter the numbers separated by space: ")].split()
    numbers = [int(num) for num in numbers]
    delimiter = int(input("Enter the delimiter: "))
    print("Resultant list: ", intersperse(numbers, delimiter))
```
In this code:

*   We define the `intersperse` function, which iterates through the input list `numbers`.
*   For each number in the list, we append it to the result list.
*   If the current number is not the last element in the list, we append the delimiter to the result list.
*   We provide test cases to verify the correctness of the function.
*   We include a simple command-line interface to allow users to input numbers and a delimiter.
*   Finally, we print the resultant list with the delimiter inserted.