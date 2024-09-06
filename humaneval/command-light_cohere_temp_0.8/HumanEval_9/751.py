```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in a given list of integers """
    return [x for x, i in enumerate(sorted(numbers), reverse=True) if numbers[i] <= numbers[i+1] and i+1 < len(numbers)]

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [3, 2, 1]
numbers3 = [4, 5, 6]

rolling_max_results1 = rolling_max(numbers1)
rolling_max_results2 = rolling_max(numbers2)
rolling_max_results3 = rolling_max(numbers3)

print("Test case 1 results: ", end="")
print(*rolling_max_results1)
print("\n")
print("Test case 2 results: ", end="")
print(*rolling_max_results2)
print("\n")
print("Test case 3 results: ", end="")
print(*rolling_max_results3)
``` 
This code provides a function `rolling_max` that generates a list of rolling maximum elements in a given list of integers. The function uses a `enumerize` function to iterate through the list, comparing each element with its previous one to determine the maximum value. The test cases demonstrate the example usage of the function, passing different lists of integers and printing the results.