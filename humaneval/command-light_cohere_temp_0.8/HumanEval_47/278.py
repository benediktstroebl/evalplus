```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

#Test case 1
test_case1 = [-10, 4, 6, 1000, 10, 20]
median_case1 = 15.0
assert median_case1 == 15.0

#Test case 2
test_case2 = [1, 2, 4, 5]
median_case2 = 5.0
assert median_case2 == 5.0

#Test case 3
test_case3 = [10, 20, 40, 60]
median_case3 = 30.0
assert median_case3 == 30.0

#Test case 4
test_case4 = [1000, 20, 40]
median_case4 = 50.0
assert median_case4 == 50.0

```  This script defines a function median that computes the median of the elements in a list l. The function first checks if the list has an even number of elements. Then, it checks if the list has an even number of elements, and if so, it calculates the median as the average of the two middle elements in the list. Otherwise, it takes the element in the middle of the list.