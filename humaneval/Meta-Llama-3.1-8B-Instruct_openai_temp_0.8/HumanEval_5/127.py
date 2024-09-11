```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    if not numbers:  # if the input list is empty
        return numbers  # return the empty list as is

    result = [numbers[0]]  # start with the first element of the input list
    for num in numbers[1:]:  # iterate over the rest of the input list
        result.append(delimeter)  # insert the delimeter
        result.append(num)  # append the current number
    return result  # return the modified list


# Test cases
if __name__ == "__main__":
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function as specified, along with two test cases to verify its correctness. The function works by initializing the result list with the first element of the input list, then iterating over the rest of the input list, inserting the delimeter and the current number at each step. If the input list is empty, it simply returns the empty list.