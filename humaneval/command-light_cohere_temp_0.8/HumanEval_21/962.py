Here is a self-contained Python function that solves the problem:
```python
def rescale_to_unit(numbers: List[float]):
    # Initialize result list to [1.0]
    smallest_number = min(numbers)
    result_list = [1.0] + [numbers[ (numbers > smallest_number)]
    while any(numbers):
        smallest_number = min(numbers)
        result_list.append(numbers[0.0])
       0.0, 0.0, 0.0] = 0.0
        result_numbers[numbers > smallest_number)
        result_list.append(numbers[0.0])
   0.0, 0])
    return result_list
```
This function takes a list of numbers and returns a list of numbers after applying a linear transform to that list. The function first adds 1 to the smallest number and then filters out the numbers that are greater than the smallest number. 

The function then adds 0 to the numbers and filters out the numbers that are greater than the smallest number. 

The function then returns the resulting list of numbers.