```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test suite for median function
def test_median():
    try:
        list1 = [-10, 4, 6, 1000, 10, 20]
        result = median(list1)
        assert result == 15.0, "Error in calculating median"

        list2 = [3, 1, 2, 4, 5]
        result = median(list2)
        assert result == 5.0, "Error in calculating median"

        list3 = [10, 20, 30, 40, 50]
        result = median(list3)
        assert result == 30.0, "Error in calculating median"

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Run the test suite
test_median()
``` 
This script defines a function `median` that calculates the median of the elements in a list, and tests its functionality with three different lists. The `test_median` function contains the test suite for the `median` function. It creates lists with different values and then checks if the calculated median matches the expected result.