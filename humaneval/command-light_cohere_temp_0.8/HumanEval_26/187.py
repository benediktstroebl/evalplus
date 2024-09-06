```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 2, 3, 1]
    result = remove_duplicates(numbers)
    assert len(result) == 3  # Verify length is correct
    assert result == [1, 3, 4]  # Verify the result
def main():
    print("Removing duplicates...")
    print("Input:", end='')
    input_str = input()
    input_numbers = [int(num) for num in input_str.split()]
   
print("Output:", end='')
    result = remove_duplicates(input_numbers)
    print(result)
if __name__ == "__main__":
    main()
``` 
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers from the original list. It uses a same set to keep track of the seen numbers and then filters out any duplicate numbers, ensuring that only the first occurrence of each unique number is retained.