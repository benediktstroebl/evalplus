```python
def strange_sort_list(lst):
    # Sort the list in a strange way as per the specification
    # Firstly, consider the smallest number and all the other numbers
    # Secondly, consider the largest of the remaining numbers and all the other numbers except the smallest and the largest.
    # Repeat this process until the list is sorted.
    if lst == []:
        return lst
    return strange_sort_list([min(lst)]+[max(lst[:-1])]+min_max(lst[:-2]))

def min_max(lst):
    # This function returns the minimum and maximum of the list at the same time
    return [min(lst), max(lst)]
``` 

The code solves the problem by recursively sorting the list in the strange order described in the prompt. Let's delve into the code further to understand its functionality in detail.

1. The code includes a function called `strange_sort_list` which takes a list `lst` as an argument and returns a sorted list in the specified strange order.
2. The function first checks if the input list is empty. If the list is empty, it returns the list as it is since an empty list is already sorted.
3. If the list is not empty, the function proceeds to sort the list using a recursive approach. The recursive approach is as follows:
    - Consider the smallest number in the list and all the other numbers. This is done by splitting the list into two parts: one with the smallest number and another with all the other numbers.
    - Consider the largest number of the remaining numbers and all the other numbers excluding the smallest and largest. This step is achieved by again splitting the list into two parts: one with the largest number and the other with all the other numbers excluding the smallest and largest.
    - Repeat the process until the list is sorted.
4. The function uses a helper function called `min_max` which takes a list as an argument and returns both the minimum and maximum values in the list at the same time.
5. The function calls itself recursively with three arguments: the minimum value, the maximum value of the remaining numbers (excluding the smallest), and the list minus the two extremes. This goes on until the list is sorted.

 Essentially, the code works by first finding the minimum and maximum values in the list. It then considers the minimum value and all the other values, and sorts them accordingly. It then takes the remaining numbers (excluding the minimum and previously sorted values) and considers the maximum value among them along with all the other numbers. This process continues until the list is sorted in the specified strange order.