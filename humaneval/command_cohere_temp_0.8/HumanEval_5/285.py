```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an interspersing delimiter `delimiter` as parameters. It initializes an empty list `result` to store the interspersed numbers. It uses a list comprehension to filter out the delimiter from the `numbers` list, creating a new list with all numbers except the delimiter. Then, it extends the `result` list with repeated instances of the delimiter, using the formula (`len(numbers) - len(result)`), to ensure the correct number of delimiter instances are added. The function returns the `result` list, which contains the numbers from `numbers` interspersed with the delimiter. 

If the input list is empty, the function returns an empty list since there are no elements to intersperse. If the input list contains only delimiters, the function returns a list with all delimiters added equally spaced to the result.