Here is a Python script that includes a self-contained function with the capability to calculate Mean Absolute Deviation:
```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    return MAD

def test():
    # create a list of numbers
    numbers = [1.0, 2.0, 3.0, 4.0]
   
   2.0]
    test numbers = List[numbers]
    # pass the list of numbers to the mean_absolute_deviation function
    result = mean_absolute_deviation(numbers)
    print(f"result: {result}")

def main():
    test()
    print("Press enter to continue...")

if __name__ == "__main__":
    main()
```
The function 'mean_absolute_deviation' uses the Mean Absolute Deviation formula to compute the MAD, which is the average absolute difference between each data point and the mean of the dataset. The MAD is calculated by computing the absolute difference between each element in the list and the mean, then taking the average of these absolute differences.

The 'test' function creates a list of numbers [1.0, 2.0, 3.0, 4.0] and passes the one list to the 'mean_absolute_deviation' function, and the result is stored in the 'result' variable. Finally, the result is printed to the console.

This code will create a list of numbers, then pass this list to the 'mean_absolute_deviation' function to calculate the Mean Absolute Deviation, and finally, print the result.